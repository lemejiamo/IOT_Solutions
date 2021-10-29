 #!/usr/bin/python3

from flask import request, make_response, jsonify, render_template, flash
from api.v1.views import app_views, views
from models.companies import Company
from models.campus import Campus
from models.users import User
from api.v1.app import load_user
from models import storage
from flask_login import current_user

@views.route('/sign-up/company', methods=['POST', 'GET'])
def new_company():
    if request.method == 'POST':
        MODELS = {
            'Company': [('NIT', 'NIT'), ('name', 'company_name'), ('telephone', 'company_telephone'), ('email', 'company_email'), ('address', 'company_address'), ('id', 'NIT')],
            'User': [('id', 'user_id'), ('user_email', 'user_email'), ('password', 'user_password'), ('company_id', 'NIT'), ('campus_id', 'campus_id'), ('telephone', 'user_telephone')],
            'Campus': [('id', 'campus_id'), ('company_id', 'NIT'), ('name', 'campus_name')],
        }

        print("\n\n\n",request.form,"\n\n\n")
        data = request.form

        def _exceptions(attribute, value):
            if attribute == 'NIT':
                if storage.get_one('Company', value):
                    print('entro')
                    flash('Company already exists!', category="error")
                if len(value) < 9:
                    flash('Wrong NIT please verify the NIT number')

            if attribute == 'company_name':
                if value is None:
                    flash('Missing Company Name')

            if attribute == 'company_telephone':
                if value is None:
                    flash('Missing Company Telephone')
                if len(value) != 10:
                    flash('Please verify telephone number')

            if attribute == 'company_email':
                if value is None:
                    flash('Missing Company Email')

            if attribute == 'company_address':
                if value is None:
                    flash('Missing Company address')

            if attribute == 'campus_id':
                if value is None:
                    flash('Missing Campus ID')

            if attribute == 'campus_name':
                if value is None:
                    flash('Missing Campus Name')

            if attribute == 'user_role':
                if value not in ['1', '0']:
                    flash('Invalid Role!', category="error")
                if value is None:
                    flash('Missing User Role')

            if attribute == 'user_id':
                if value is None:
                    flash('Missing User ID')

            if attribute == 'user_email':
                if len(value) < 3 or User.get_user(value) is not None:
                    flash('email too short or the email already exists!', category="error")
                if value is None:
                    flash('Missing user email')

            if attribute == 'user_password':
                if len(value) < 4:
                    flash('password too short!', category="error")
                if value is None:
                    flash('Missing user password')

            if attribute == 'password2':
                #if password != password2 :
                   #flash('email doesn\'t match!', category="error")
                if value is None:
                    flash('Missing confirmation password')

            if attribute == 'user_telephone':
                if len(value) < 10:
                    flash('Telephone number too short!', category="error")
                if value is None:
                    flash('Missing user telephone')

            print('no exceptions found {}'.format(attribute))

        for key, value in data.items():
            print('key {} type{}, value {} type{}'.format(key, value, type(key), type(value)))
            _exceptions(key, value)

        company_data = {}
        user_data = {}
        campus_data =  {}
        for key, value in MODELS.items():
            if key == 'Company':
                for value_key in value:
                    company_data[value_key[0]] = data.get(value_key[1])
                print (company_data)
            if key == 'User':
                for value_key in value:
                    user_data[value_key[0]] = data.get(value_key[1])
                print (user_data)
            if key == 'Campus':
                for value_key in value:
                    campus_data[value_key[0]] = data.get(value_key[1])
                print (campus_data)

        company = Company(**company_data)
        company.save()
        campus = Campus(**campus_data)
        campus.save()
        user = User(**user_data)
        user.save()
        flash("Sucesful created in data base")
        #return (make_response(jsonify('Sucesful created in data base', 202)))
    return render_template("company_signup.html", user=current_user)
