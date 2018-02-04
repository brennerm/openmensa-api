# OpenMensa API
This project is a Python wrapper for the [OpenMensa API v2](http://doc.openmensa.org/api/v2/).

## Installation
```
$ pip install openmensa-api
```
## [API Documentation](https://brennerm.github.io/openmensa-api/openmensa/)

## Example
```python
>>> from openmensa import OpenMensa as OM
>>> OM.get_canteen(63)
{  
  'id':63,
  'coordinates':[  
    51.3374622576675,
    12.3781263828278
  ],
  'address':'Universitätsstraße 5, 04109 Leipzig',
  'city':'Leipzig',
  'name':'Leipzig, Mensa am Park'
}

>>> OM.get_meals_by_day(63, '2018-02-05')
[  
  {  
    'id':3035676,
    'notes':[  
      'Geflügel',
      'Sesam',
      'Eier',
      'glutenhaltiges Getreide',
      'gebackene Kartoffelspalten',
      'Kaisergemüse',
      'Geflügelsoße'
    ],
    'prices':{  
      'pupils':None,
      'others':6.5,
      'employees':4.7,
      'students':2.85
    },
    'category':'Schneller Teller',
    'name':'Hähnchenbrust in Sesampanade'
  },
  {  
    'id':3035677,
    'notes':[  
      'Fisch',
      'Senf',
      'Milch/ Milchzucker',
      'Fisch',
      'glutenhaltiges Getreide',
      'mit Farbstoff',
      'Karottengemüse',
      'Salzkartoffeln',
      'Paprikareis',
      'Brokkoligemüse',
      'Schnittlauch-Sahnesoße'
    ],
    'prices':{  
      'pupils':None,
      'others':7.0,
      'employees':5.0,
      'students':3.15
    },
    'category':'Fischgericht',
    'name':'Kabeljaufilet Müllerinart'
  },
  {  
    'id':3035678,
    'notes':[  
      'Rind',
      'Schwein',
      'Fleischloses Gericht',
      'Eier',
      'Milch/ Milchzucker',
      'glutenhaltiges Getreide',
      'mit Farbstoff',
      'Kochklopse Königsberger Art mit Kapernsoße'
    ],
    'prices':{  
      'pupils':None,
      'others':3.2,
      'employees':2.4,
      'students':1.65
    },
    'category':'Hauptkomponente',
    'name':'Kapernsoße'
  },
  {  
    'id':3035679,
    'notes':[  
      'Veganes Gericht',
      'Schwein'
    ],
    'prices':{  
      'pupils':None,
      'others':1.25,
      'employees':0.9,
      'students':0.5
    },
    'category':'Gemüsebeilage',
    'name':'Karottengemüse'
  },
  {  
    'id':3035680,
    'notes':[  
      'Veganes Gericht',
      'Schwein'
    ],
    'prices':{  
      'pupils':None,
      'others':1.25,
      'employees':0.9,
      'students':0.5
    },
    'category':'Gemüsebeilage',
    'name':'Wirsingkohl mit Speck'
  },
  {  
    'id':3035681,
    'notes':[  
      'Veganes Gericht',
      'Schwein'
    ],
    'prices':{  
      'pupils':None,
      'others':1.25,
      'employees':0.9,
      'students':0.5
    },
    'category':'Gemüsebeilage',
    'name':'Pariser Karotten'
  },
  {  
    'id':3035682,
    'notes':[  

    ],
    'prices':{  
      'pupils':None,
      'others':1.45,
      'employees':1.1,
      'students':0.7
    },
    'category':'Gemüsebeilage',
    'name':'Brokkoligemüse'
  },
  {  
    'id':3035683,
    'notes':[  
      'Sulfit/ Schwefeldioxid',
      'Milch/ Milchzucker',
      'mit Antioxidationsmitteln',
      'mit Farbstoff',
      'Fleischloses Gericht',
      'Veganes Gericht'
    ],
    'prices':{  
      'pupils':None,
      'others':1.25,
      'employees':0.9,
      'students':0.5
    },
    'category':'Sättigungsbeilage',
    'name':'Paprikareis'
  },
  {  
    'id':3035684,
    'notes':[  
      'Sulfit/ Schwefeldioxid',
      'Milch/ Milchzucker',
      'mit Antioxidationsmitteln',
      'mit Farbstoff',
      'Fleischloses Gericht',
      'Veganes Gericht'
    ],
    'prices':{  
      'pupils':None,
      'others':1.25,
      'employees':0.9,
      'students':0.5
    },
    'category':'Sättigungsbeilage',
    'name':'Petersilienkartoffeln'
  },
  {  
    'id':3035685,
    'notes':[  
      'Sulfit/ Schwefeldioxid',
      'Milch/ Milchzucker',
      'mit Antioxidationsmitteln',
      'mit Farbstoff',
      'Fleischloses Gericht',
      'Veganes Gericht'
    ],
    'prices':{  
      'pupils':None,
      'others':1.25,
      'employees':0.9,
      'students':0.5
    },
    'category':'Sättigungsbeilage',
    'name':'Salzkartoffeln'
  },
  {  
    'id':3035686,
    'notes':[  
      'Sulfit/ Schwefeldioxid',
      'Milch/ Milchzucker',
      'mit Antioxidationsmitteln',
      'mit Farbstoff',
      'Fleischloses Gericht',
      'Veganes Gericht'
    ],
    'prices':{  
      'pupils':None,
      'others':1.25,
      'employees':0.9,
      'students':0.5
    },
    'category':'Sättigungsbeilage',
    'name':'Kartoffelpüree'
  },
  {  
    'id':3035687,
    'notes':[  

    ],
    'prices':{  
      'pupils':None,
      'others':1.45,
      'employees':1.1,
      'students':0.7
    },
    'category':'Sättigungsbeilage',
    'name':'gebackene Kartoffelspalten'
  },
  {  
    'id':3035688,
    'notes':[  
      'mit Farbstoff',
      'Fleischloses Gericht',
      'Milch/ Milchzucker',
      'Eier',
      'glutenhaltiges Getreide',
      'Tomatensoße'
    ],
    'prices':{  
      'pupils':None,
      'others':5.5,
      'employees':3.8,
      'students':1.95
    },
    'category':'Vegetarisches Gericht',
    'name':'Gemüseauflauf mit Hirtenkäse & Reis'
  },
  {  
    'id':3035689,
    'notes':[  
      'Soja',
      'mit Antioxidationsmitteln',
      'Veganes Gericht',
      'gebackene Kartoffelspalten',
      'Ingwer-Möhrensoße'
    ],
    'prices':{  
      'pupils':None,
      'others':7.0,
      'employees':5.0,
      'students':3.2
    },
    'category':'Veganes Gericht',
    'name':'Gebratener Fenchel'
  },
  {  
    'id':3035690,
    'notes':[  
      'mit Antioxidationsmitteln',
      'mit Farbstoff',
      'Veganes Gericht',
      'Soja',
      'Milch/ Milchzucker',
      'glutenhaltiges Getreide'
    ],
    'prices':{  
      'pupils':None,
      'others':5.2,
      'employees':3.7,
      'students':1.9
    },
    'category':'Pastateller',
    'name':'Spaghetti'
  },
  {  
    'id':3035691,
    'notes':[  
      'mit Antioxidationsmitteln',
      'mit Farbstoff',
      'Veganes Gericht',
      'Soja',
      'Milch/ Milchzucker',
      'glutenhaltiges Getreide'
    ],
    'prices':{  
      'pupils':None,
      'others':5.2,
      'employees':3.7,
      'students':1.9
    },
    'category':'Pastateller',
    'name':'Muschelnudeln'
  },
  {  
    'id':3035692,
    'notes':[  
      'mit Antioxidationsmitteln',
      'mit Farbstoff',
      'Veganes Gericht',
      'Soja',
      'Milch/ Milchzucker',
      'glutenhaltiges Getreide'
    ],
    'prices':{  
      'pupils':None,
      'others':5.2,
      'employees':3.7,
      'students':1.9
    },
    'category':'Pastateller',
    'name':'bunte Farfalle'
  },
  {  
    'id':3035693,
    'notes':[  
      'mit Antioxidationsmitteln',
      'mit Farbstoff',
      'Veganes Gericht',
      'Soja',
      'Milch/ Milchzucker',
      'glutenhaltiges Getreide'
    ],
    'prices':{  
      'pupils':None,
      'others':5.2,
      'employees':3.7,
      'students':1.9
    },
    'category':'Pastateller',
    'name':'Tomatensoße'
  },
  {  
    'id':3035694,
    'notes':[  
      'mit Antioxidationsmitteln',
      'mit Farbstoff',
      'Veganes Gericht',
      'Soja',
      'Milch/ Milchzucker',
      'glutenhaltiges Getreide'
    ],
    'prices':{  
      'pupils':None,
      'others':5.2,
      'employees':3.7,
      'students':1.9
    },
    'category':'Pastateller',
    'name':'Currysoße'
  },
  {  
    'id':3035695,
    'notes':[  
      'mit Antioxidationsmitteln',
      'mit Farbstoff',
      'Veganes Gericht',
      'Soja',
      'Milch/ Milchzucker',
      'glutenhaltiges Getreide'
    ],
    'prices':{  
      'pupils':None,
      'others':5.2,
      'employees':3.7,
      'students':1.9
    },
    'category':'Pastateller',
    'name':'Tomatensoße mit Ingwer'
  },
  {  
    'id':3035696,
    'notes':[  
      'Geflügel',
      'Schwein',
      'Sellerie',
      'Milch/ Milchzucker',
      'glutenhaltiges Getreide',
      'mit Antioxidationsmitteln',
      'mit Konservierungsstoff',
      'mit Farbstoff'
    ],
    'prices':{  
      'pupils':None,
      'others':3.25,
      'employees':2.65,
      'students':1.5
    },
    'category':'Pizza',
    'name':'Pizza Italia'
  },
  {  
    'id':3035697,
    'notes':[  
      'Geflügel',
      'Schwein',
      'Sellerie',
      'Milch/ Milchzucker',
      'glutenhaltiges Getreide',
      'mit Antioxidationsmitteln',
      'mit Konservierungsstoff',
      'mit Farbstoff'
    ],
    'prices':{  
      'pupils':None,
      'others':3.25,
      'employees':2.65,
      'students':1.5
    },
    'category':'Pizza',
    'name':'Pizza Venedig'
  },
  {  
    'id':3035698,
    'notes':[  
      'Geflügel',
      'Schwein',
      'Sellerie',
      'Milch/ Milchzucker',
      'glutenhaltiges Getreide',
      'mit Antioxidationsmitteln',
      'mit Konservierungsstoff',
      'mit Farbstoff'
    ],
    'prices':{  
      'pupils':None,
      'others':3.25,
      'employees':2.65,
      'students':1.5
    },
    'category':'Pizza',
    'name':'Pizza Heideland'
  }
]
```