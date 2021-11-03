from hashlib import new
from flask import request, render_template, flash, redirect, url_for
from api.v1.views import views
from models.users import User
from models import storage
from flask_login import login_required, current_user
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from datetime import datetime
import seaborn as sns
import io
import base64

@views.route("/user_home", methods=['GET', 'POST'])
@login_required
def home():

    if current_user.rol:
        all_campuses = storage.get_objects("Campus").values()
        if current_user.user_email == "admin@iotsolutions.com":
            campuses = all_campuses
        else:
            campuses = [campus for campus in all_campuses if campus.company_id == current_user.company_id]


    else:
        campuses = [storage.get_one("Campus", current_user.campus_id)]
    if request.method == 'POST':
        id = request.form.get("id")
        if len(id) >= 1:
            if storage.get_one("Device", int(id)) != None:
                return redirect(url_for("views.device_records", id=id))
        flash("Put a valid device Id to search", category="error")
    return render_template("user_home.html", user=current_user, campuses=campuses)


@views.route("/device/<id>", methods=['GET', 'POST'])
@login_required
def device_records(id):
    device = storage.get_one("Device", int(id))
    records = device.TEMP
    df = pd.DataFrame([[record.measure, record.date] for record in records], columns = ['Temp', 'Date'])

    if request.method == 'POST':
        filtered_df = df.loc[(df['Date'] >= '2021-08-10')
                    & (df['Date'] < '2021-08-15')]
    else:
        # print(df.dtypes)
        filter = "{}-{}-01".format(datetime.now().year, datetime.now().month)
        filtered_df = df.loc[(df['Date'] >= filter)]

    figure = sns.lineplot(x = "Date", y = "Temp", data = filtered_df)
    plt.title("{} {} for {} in {}".format(datetime.now().strftime("%B"),
                                          "Temp", device.location, device.area))
    if len(filtered_df["Temp"]) > 0:
        date_form = DateFormatter("%b-%d")
        figure.xaxis.set_major_formatter(date_form)
    buf = io.BytesIO()
    figure.get_figure().savefig(buf, format='png')
    buf.seek(0)
    buffer = b''.join(buf)
    b2 = base64.b64encode(buffer)
    graph = b2.decode('utf-8')

    table=[]
    table.append(filtered_df["Temp"])
    table.append(pd.to_datetime(filtered_df["Date"]).dt.strftime("%B-%d"))
    table.append(pd.to_datetime(filtered_df["Date"]).dt.strftime("%H:%M"))

    return render_template("device_records.html", user=current_user,
                            device=device, table=table, graph=graph, size=len(table[0]))
