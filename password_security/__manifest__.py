# Copyright 2015 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{

    'name': 'Password Security',
    "summary": "Allow admin to set password security requirements.",
    'version': '11.0.1.1.1',
    'author':
        "LasLabs, "
        "Kaushal Prajapati, "
        "Tecnativa, "
        "Odoo Community Association (OCA)",
    'category': 'Base',
    'depends': [
        'auth_crypt',
        'auth_signup',
    ],
    "website": "https://laslabs.com",
    "license": "LGPL-3",
    "data": [
        'views/res_company_view.xml',
        'security/ir.model.access.csv',
        'security/res_users_pass_history.xml',
    ],
    "demo": [
        'demo/res_users.xml',
    ],
    'installable': True,
}