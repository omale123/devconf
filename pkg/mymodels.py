import datetime
from pkg import db


class State(db.Model): 
    state_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    state_name = db.Column(db.String(255), nullable=False)

class Lga(db.Model): 
    lga_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    state_id = db.Column(db.String(255), nullable=False)
    lga_name= db.Column(db.Integer(),db.ForeignKey('state.state_id'),nullable=False)

    thestate = db.relationship('State',backref='lgadeets')



class Transaction(db.Model):
    trx_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    trx_user = db.Column(db.Integer(),db.ForeignKey("user.user_id"), nullable=False)
    trx_refno = db.Column(db.String(255), nullable=True)
    trx_totalamt = db.Column(db.Float(), nullable=True)
    trx_status = db.Column(db.Enum("pending","paid","faild"), nullable=True)
    trx_method = db.Column(db.Enum("card","cash"), nullable=True)
    trx_paygate = db.Column(db.Text(), nullable=True)
    trx_date = db.Column(db.DateTime(), default=datetime.datetime.utcnow())

    user_whopaid = db.relationship("User",backref="mytrxs")



class Products(db.Model): 
    product_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    product_name = db.Column(db.String(255), nullable=False)
    product_price= db.Column(db.Float(), nullable=False)

class Plang(db.Model): 
    
    plang_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    plang_name = db.Column(db.String(255), nullable=False)
    plang_desc = db.Column(db.String(255), nullable=True)

  

class Userlang(db.Model):
    userlang_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    userlang_plang = db.Column(db.Integer(),db.ForeignKey('plang.plang_id'), nullable=False)
    userlang_user= db.Column(db.Integer(),db.ForeignKey('user.user_id'),nullable=False)

    userdeet = db.relationship('User',backref='langes')
    langdeets= db.relationship('Plang',backref='users')

class User(db.Model): 
    user_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    user_email = db.Column(db.String(255), nullable=False)
    user_pass = db.Column(db.String(255), nullable=False)
    user_image = db.Column(db.String(255), nullable=False)
    user_fname = db.Column(db.String(255), nullable=False)
    user_lname = db.Column(db.String(255), nullable=False)
    user_state = db.Column(db.Integer(),db.ForeignKey('state.state_id'),nullable=True)
    user_phone = db.Column(db.String(100), nullable=True)
    user_reg = db.Column(db.DateTime(), default=datetime.datetime.utcnow())
    '''set to join relationship between user and state'''
    '''mystate = db.relationship('State',backref='theusers')'''


class Admin(db.Model): 
    admin_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    admin_username = db.Column(db.String(255), nullable=False)
    admin_password = db.Column(db.String(255), nullable=False)
    admin_lastlogin = db.Column(db.DateTime(), onupdate=datetime.datetime.utcnow())


class Purchases(db.Model):
    pur_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    pur_userid = db.Column(db.Integer(), db.ForeignKey('user.user_id'), nullable=False)
    pur_product_id = db.Column(db.Integer(), db.ForeignKey('products.product_id'), nullable=False)
    pur_trxid = db.Column(db. Integer(), db.ForeignKey('transaction.trx_id'), nullable=False)


    userdeets = db.relationship('User',backref='prods')
    proddeets = db.relationship('Products',backref='users')
    transdeets= db.relationship('Transaction',backref='purchases_deets')



class Posts(db.Model): 
    post_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    post_title = db.Column(db.String(100), nullable=False)
    post_content = db.Column(db.Text(), nullable=False)
    post_userid = db.Column(db.Integer(), db.ForeignKey('user.user_id'),nullable=False)
    post_date = db.Column(db.DateTime(), default=datetime.datetime.utcnow())
    '''set to join relationship between user and post'''
    postuser = db.relationship('User',backref='myposts')



class Comment(db.Model): 
    comment_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    comment_by = db.Column(db.Integer(),db.ForeignKey('user.user_id'), nullable=False)
    comment_content = db.Column(db.Text(), nullable=False)
    comment_postid = db.Column(db.Integer(), db.ForeignKey('posts.post_id'),nullable=False)
    comment_date = db.Column(db.DateTime(), default=datetime.datetime.utcnow())
    '''set to join relationship between user and post'''
    dpost = db.relationship('Posts',backref='comments')
    commentuser = db.relationship('User',backref='mycomments')
    
    