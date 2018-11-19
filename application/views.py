from flask import request, render_template, redirect, url_for
from application import app
from application.models import fhrapi
from forms import SearchForm



#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/', methods=['POST', 'GET'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('results',
                                postcode=form.postcode.data))
    return render_template('pages/home.html',
                           form=form)


@app.route('/results')
@app.route('/results/<int:page>')
def results(page=1):
    pc = request.args.get('postcode')
    m_restaurants = fhrapi.RestaurantData()
    list_restaurants = m_restaurants.get_establishments(page=page, pc=pc)
    meta = m_restaurants.get_establishments_meta()
    last_page = meta['totalPages']
    totalCount = meta['totalCount']
    return render_template('pages/results.html',
                           list_restaurants=list_restaurants,
                           page=page,
                           last_page=last_page,
                           totalCount=totalCount,
                           postcode=pc)

@app.route('/filters', methods=['POST'])
def filters():
    search_text = request.form['search_text']
    pc = request.form['pc']
    # rating = request.form['rating']
    m_restaurants = fhrapi.RestaurantData()
    list_restaurants = m_restaurants.get_establishments(pc=pc, searchtext=search_text)
    meta = m_restaurants.get_establishments_meta()
    last_page = meta['totalPages']
    totalCount = meta['totalCount']
    return render_template('pages/results_filter.html',
                           list_restaurants=list_restaurants,
                           page=1,
                           last_page=last_page,
                           totalCount=totalCount)
