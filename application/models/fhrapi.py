import requests
import re
from time import strptime, strftime
from application import db
import pc_lookup



class RestaurantData():
    # API request headers
    headers = {
        "content-type": "application/json",
        "x-api-version": "2",
        "accept": "application/json"
    }

    def format_address(self, al1, al2, al3, al4, pc):
        l = []
        al1 = al1
        al2 = al2
        al3 = al3
        al4 = al4
        pc = pc

        if al1:
            l.append(al1)
        if al2:
            l.append(al2)
        if al3:
            l.append(al3)
        if al4:
            l.append(al4)
        if pc:
            l.append(pc)
        s = ', '.join(l)
        return s

    def get_establishments(self, pc, page=1, searchtext='', rating=''):
        geo = pc_lookup.postcode_lookup(pc)
        lat = geo['lat']
        lng = geo['long']
        # Set parameters for api call
        parameters = {
            "latitude": lat,
            "longitude": lng,
            "maxDistanceLimit": "5",
            "pageSize": "10",
            "sortOptionKey": "Relevance",
            "pageNumber": page,
            "name": searchtext
            # "ratingKey": rating
        }

        # Make a request to FHR api
        response = requests.get('http://api.ratings.food.gov.uk/Establishments',
                                params=parameters, headers=self.headers)
        data = response.json()

        # Put Json in list
        lestablishments = []
        for establishments in data['establishments']:
            results = dict()
            RatingDate = strptime(establishments["RatingDate"], '%Y-%m-%dT%H:%M:%S')
            ddmmyy = strftime('%d/%m/%Y', RatingDate)
            # results['BusinessName'] = establishments["BusinessName"]
            results['BusinessName'] = re.sub("[^ 'a-zA-Z0-9]", "", establishments["BusinessName"])
            results['BusinessType'] = BusinessType().get_business_type(
                establishments["BusinessTypeID"])
            results['AddressLine1'] = self.format_address(al1=establishments["AddressLine1"],
                                                          al2=establishments["AddressLine2"],
                                                          al3=establishments["AddressLine3"],
                                                          al4=establishments["AddressLine4"],
                                                          pc=establishments["PostCode"])
            results['RatingValue'] = establishments["RatingValue"]
            results['RatingDate'] = ddmmyy
            results['BusinessTypeID'] = establishments["BusinessTypeID"]
            results['img'] = self.rating_image(establishments["RatingValue"])
            lestablishments.append(results)
        return lestablishments

    def get_establishments_meta(self):
        # Set parameters for api call
        parameters = {
            "latitude": "51.65980",
            "longitude": "0.03610",
            "maxDistanceLimit": "10",
            "pageSize": "10",
            "sortOptionKey": "rating",
            "pageNumber": "1",
            "ratingKey": "5"
        }

        # Make a request to FHR api
        response = requests.get('http://api.ratings.food.gov.uk/Establishments',
                                params=parameters, headers=self.headers)
        data = response.json()

        meta = dict()

        meta['totalPages'] = data['meta']['totalPages']
        meta['totalCount'] = data['meta']['totalCount']

        return meta

    def rating_image(self, rating):
        r = rating
        if r == '1':
            return '/static/img/fhrs_1_en-gb.jpg'
        elif r == '2':
            return '/static/img/fhrs_2_en-gb.jpg'
        elif r == '3':
            return '/static/img/fhrs_3_en-gb.jpg'
        elif r == '4':
            return '/static/img/fhrs_4_en-gb.jpg'
        elif r == '5':
            return '/static/img/fhrs_5_en-gb.jpg'
        elif r == '0':
            return '/static/img/fhrs_0_en-gb.jpg'
        else:
            return '/static/img/fhrs_1_en-gb.jpg'


class BusinessType(db.Model):
    __tablename__ = "fhr_business_type"
    business_type_id = db.Column(db.Integer, primary_key=True)
    business_type_name = db.Column(db.String(50))

    def get_business_type(self, business_type_id):
        # Make a request to FHR api
        output = db.session.query(BusinessType.business_type_name).filter(
            BusinessType.business_type_id == business_type_id).limit(1).scalar()
        return output
