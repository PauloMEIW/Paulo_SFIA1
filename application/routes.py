from flask import render_template, redirect, url_for, request
from application import db, app, bcrypt
from application.models import Favou, Reviews, Users, Products
from application.forms import ReviewForm, RegistrationForm, LoginForm, UpdateAccountForm, UpdateStoreForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
      return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(
        first_name=form.first_name.data,
        last_name=form.last_name.data,
        email=form.email.data,
        password=hash_pw)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

#favourites__________________________________________
#add


@app.route('/favou/<id>/<productcode>', methods=["GET"])
@login_required
def favou_add(id,productcode):
    product = products.query.filter_by(productcode=productcode).first()
    user = users.query.filter_by(id=id).first()
    if user and product():
     favou(user=user,product=product)
     db.session.add(favouid)
     db.session.commit()
    return redirect(url_for('account'))

#delete

@app.route('/favou/<id>/<productcode>', methods=["GET"])
@login_required
def favou_delete(id,productcode):
    product = products.query.filter_by(productcode=productcode).first()
    user = users.query.filter_by(id=id).first()
    if user and product():
     favou(user=user,product=product)
     db.session.delete(favouid)
     db.session.commit()
    return redirect(url_for('account'))




#reviews_____________________________________________________________
@app.route('/review', methods=['GET', 'POST'])
@login_required
def review():
    form = ReviewForm()
    reviews = Reviews.query.all()
    if form.validate_on_submit():
        reviewData = Reviews(
            title = form.title.data,
            content = form.content.data,
            author = current_user
 )
        db.session.add(reviewData)
        db.session.commit()
        return redirect(url_for('review'))
    else:
        print(form.errors)
    return render_template('review.html', title='Review', form=form, reviews=reviews)

#delete review
@app.route("/review/delete/<id>", methods=["GET"])
@login_required
def review_delete(id):
    review = Reviews.query.filter_by(id=id).first()
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for('review'))

@app.route('/home')
def home():
    reviewdata=Reviews.query.all()
    return render_template('home.html', title='Home', form=reviewdata)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


#STORE____________________________________________________________________
#add
@app.route('/store', methods=['GET', 'POST'])
@login_required
def store():
   form = UpdateStoreForm()
   products = Products.query.all()
   if form.validate_on_submit():
       product = Products(
           productname=form.productname.data,
           productdescription=form.productdescription.data,
           price=form.price.data,
           productvendor=form.productvendor.data
       )
       db.session.add(product)
       db.session.commit()
       return redirect(url_for('store'))
   else:
       print(form.errors)
   return render_template('store.html', title='store', form=form, products=products)


#update
@app.route('/store', methods=['GET', 'POST'])
@login_required
def store_update():
    form = UpdateStoreForm()
    if form.validate_on_submit():
        current_user.productname = form.productname.data
        current_user.productvendor = form.productvendor.data
        current_user.productdescription = form.productdescription.data
        current_user.price = form.price.data
        db.session.commit()
        return redirect(url_for('store'))
    elif request.method == 'GET':
        form.productname.data = current_user.productname
        form.productvendor.data = current_user.productvendor
        form.productdescription.data = current_user.productdescription
        form.price = current_user.price
    return render_template('store.html', title='store', form=form)

#delete
@app.route('/store', methods=["GET", "POST"])
@login_required
def store_delete():
    form = product()
    product = request.form.get('productname')
    product = Products.query.filter_by(productname=form).first()
    db.session.delete(product)
    db.session.commit()
    return render_template('store.html', title='store', form=form)


#ACCOUNT ___________________________________________________________

#update
@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)

#delete account
@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():
    user = current_user.id
    account = Users.query.filter_by(id=user).first()
    logout_user()
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('register'))



