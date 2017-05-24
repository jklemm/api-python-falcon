import falcon
import json


class QuoteResource(object):
    def on_get(self, req, resp):
        quote = {
            'quote': 'I\'ve always been more interested in the future than in the past.',
            'author': 'Grace Hopper'
        }
        resp.body = json.dumps(quote)


class QuotesResource(object):
    def on_get(self, req, resp):
        quotes = [
            {
                "_id": "5925da9b1ae60c3e63a873ea",
                "index": 0,
                "guid": "7cf2e8a5-fb9c-4a9f-b998-b12f08b80cf4",
                "isActive": False,
                "balance": "$2,007.06",
                "picture": "http://placehold.it/32x32",
                "age": 25,
                "eyeColor": "green",
                "name": "Booth Snyder",
                "gender": "male",
                "company": "EBIDCO",
                "email": "boothsnyder@ebidco.com",
                "phone": "+1 (997) 423-3853",
                "address": "848 Hutchinson Court, Finzel, American Samoa, 4984",
                "about": "Ex ex dolor adipisicing dolore laborum dolor aliquip laborum nisi et. Tempor dolor minim mollit magna. Exercitation dolore in amet ipsum id reprehenderit amet cillum incididunt ea anim aute. In dolor consequat pariatur occaecat occaecat ad sunt ad anim enim dolor. Et exercitation aute occaecat consectetur culpa cillum incididunt voluptate nostrud velit. Ut aliqua voluptate dolore minim occaecat nisi excepteur.\r\n",
                "registered": "2015-03-17T09:20:15 +03:00",
                "latitude": 86.687366,
                "longitude": -80.84081,
                "tags": [
                    "consequat",
                    "culpa",
                    "sunt",
                    "qui",
                    "tempor",
                    "exercitation",
                    "est"
                ],
                "friends": [
                    {
                        "id": 0,
                        "name": "Mollie Ryan"
                    },
                    {
                        "id": 1,
                        "name": "Margo Brady"
                    },
                    {
                        "id": 2,
                        "name": "Muriel Foley"
                    }
                ],
                "greeting": "Hello, Booth Snyder! You have 8 unread messages.",
                "favoriteFruit": "banana"
            },
            {
                "_id": "5925da9b171ef99bb5e51252",
                "index": 1,
                "guid": "d4f5b017-2e52-4922-8fed-3265578bc86a",
                "isActive": False,
                "balance": "$3,968.89",
                "picture": "http://placehold.it/32x32",
                "age": 34,
                "eyeColor": "green",
                "name": "Alejandra Langley",
                "gender": "female",
                "company": "OVOLO",
                "email": "alejandralangley@ovolo.com",
                "phone": "+1 (995) 481-3594",
                "address": "435 Cobek Court, Wacissa, Guam, 1562",
                "about": "Nulla Lorem non non voluptate consectetur non deserunt mollit veniam ipsum anim mollit dolore amet. Non nisi sint adipisicing consequat mollit magna id proident laboris. Laboris officia ex consequat reprehenderit nostrud ad nostrud proident. Enim amet aute Lorem ad adipisicing enim id dolore mollit. Adipisicing ex do occaecat ullamco aliqua occaecat veniam mollit deserunt excepteur eu officia.\r\n",
                "registered": "2016-08-18T09:56:39 +03:00",
                "latitude": -10.627609,
                "longitude": 124.516518,
                "tags": [
                    "sit",
                    "ut",
                    "ullamco",
                    "deserunt",
                    "exercitation",
                    "mollit",
                    "magna"
                ],
                "friends": [
                    {
                        "id": 0,
                        "name": "Tania Bradshaw"
                    },
                    {
                        "id": 1,
                        "name": "Florence Hardy"
                    },
                    {
                        "id": 2,
                        "name": "Durham Mullins"
                    }
                ],
                "greeting": "Hello, Alejandra Langley! You have 4 unread messages.",
                "favoriteFruit": "strawberry"
            },
            {
                "_id": "5925da9b294badd9e40730bf",
                "index": 2,
                "guid": "2e1e616d-5710-444e-b550-7e2cf0ae461a",
                "isActive": False,
                "balance": "$1,938.62",
                "picture": "http://placehold.it/32x32",
                "age": 37,
                "eyeColor": "blue",
                "name": "Martina Bean",
                "gender": "female",
                "company": "RADIANTIX",
                "email": "martinabean@radiantix.com",
                "phone": "+1 (846) 514-2067",
                "address": "334 Madison Street, Canterwood, Maryland, 4400",
                "about": "Excepteur eiusmod id dolor minim est. Aliquip velit ad in est est exercitation do ad culpa. Do voluptate pariatur elit voluptate nisi. Do aliqua aute mollit cillum laboris. Eu nostrud excepteur qui labore quis dolore elit proident pariatur. Ad ea pariatur dolor consectetur deserunt et excepteur.\r\n",
                "registered": "2016-04-11T01:42:17 +03:00",
                "latitude": -76.160874,
                "longitude": -80.56687,
                "tags": [
                    "culpa",
                    "aliquip",
                    "ut",
                    "deserunt",
                    "magna",
                    "consectetur",
                    "consectetur"
                ],
                "friends": [
                    {
                        "id": 0,
                        "name": "Kelly Walters"
                    },
                    {
                        "id": 1,
                        "name": "Stanley Mckee"
                    },
                    {
                        "id": 2,
                        "name": "Morton Brewer"
                    }
                ],
                "greeting": "Hello, Martina Bean! You have 5 unread messages.",
                "favoriteFruit": "strawberry"
            },
            {
                "_id": "5925da9b1aead3cec9fd3e59",
                "index": 3,
                "guid": "aa0ba36c-7e78-4da4-872e-9aa2611a6b41",
                "isActive": True,
                "balance": "$1,313.61",
                "picture": "http://placehold.it/32x32",
                "age": 23,
                "eyeColor": "green",
                "name": "Merrill Hammond",
                "gender": "male",
                "company": "INSURESYS",
                "email": "merrillhammond@insuresys.com",
                "phone": "+1 (888) 435-3409",
                "address": "785 Vandervoort Avenue, Shawmut, Texas, 3676",
                "about": "Qui id reprehenderit eu ut Lorem et occaecat officia nostrud elit duis. Laborum aliqua aute tempor non adipisicing nulla eu. Duis nisi consectetur occaecat aliquip sint fugiat labore mollit ut. Tempor labore eiusmod mollit occaecat consequat magna cillum commodo nisi dolor eu. Anim qui consequat quis aliqua aute et non in irure ut pariatur. Laborum ut duis magna sint qui adipisicing enim ullamco.\r\n",
                "registered": "2014-07-15T05:39:33 +03:00",
                "latitude": 64.944773,
                "longitude": 96.046587,
                "tags": [
                    "nostrud",
                    "nisi",
                    "occaecat",
                    "laborum",
                    "fugiat",
                    "eu",
                    "aliquip"
                ],
                "friends": [
                    {
                        "id": 0,
                        "name": "Marian Alvarado"
                    },
                    {
                        "id": 1,
                        "name": "Roxie Carson"
                    },
                    {
                        "id": 2,
                        "name": "Duffy Thompson"
                    }
                ],
                "greeting": "Hello, Merrill Hammond! You have 9 unread messages.",
                "favoriteFruit": "banana"
            },
            {
                "_id": "5925da9b007162d9d70ca2ca",
                "index": 4,
                "guid": "41d54b33-a51a-427d-8863-c0e57daf4878",
                "isActive": True,
                "balance": "$3,978.74",
                "picture": "http://placehold.it/32x32",
                "age": 26,
                "eyeColor": "brown",
                "name": "Craft Riddle",
                "gender": "male",
                "company": "GOLOGY",
                "email": "craftriddle@gology.com",
                "phone": "+1 (817) 434-3566",
                "address": "714 Commercial Street, Curtice, California, 9485",
                "about": "Consectetur cillum tempor eiusmod ex minim dolore nulla. Labore nostrud esse officia incididunt veniam est tempor labore excepteur quis culpa elit. Ea proident do velit pariatur nostrud.\r\n",
                "registered": "2015-12-08T01:22:33 +02:00",
                "latitude": 8.134105,
                "longitude": 45.78139,
                "tags": [
                    "fugiat",
                    "ullamco",
                    "aliquip",
                    "minim",
                    "do",
                    "sunt",
                    "ut"
                ],
                "friends": [
                    {
                        "id": 0,
                        "name": "Fischer Huber"
                    },
                    {
                        "id": 1,
                        "name": "Cassie Clements"
                    },
                    {
                        "id": 2,
                        "name": "Buck Sanford"
                    }
                ],
                "greeting": "Hello, Craft Riddle! You have 8 unread messages.",
                "favoriteFruit": "apple"
            },
            {
                "_id": "5925da9bcabfd2a012303186",
                "index": 5,
                "guid": "d53f53af-fa4a-4e0c-87f9-17d773e691f9",
                "isActive": True,
                "balance": "$2,721.89",
                "picture": "http://placehold.it/32x32",
                "age": 37,
                "eyeColor": "blue",
                "name": "Mack Larsen",
                "gender": "male",
                "company": "STRALOY",
                "email": "macklarsen@straloy.com",
                "phone": "+1 (850) 557-3257",
                "address": "728 Bulwer Place, Austinburg, Louisiana, 5667",
                "about": "Do sint sunt est do non adipisicing eiusmod minim pariatur minim non aliqua. Anim dolor magna consectetur sint esse esse ipsum. Veniam adipisicing reprehenderit minim voluptate cillum duis cillum nisi. Do consequat est non quis minim est labore laboris ut adipisicing fugiat laboris.\r\n",
                "registered": "2015-06-05T04:31:16 +03:00",
                "latitude": 32.436641,
                "longitude": -125.524589,
                "tags": [
                    "non",
                    "excepteur",
                    "enim",
                    "eiusmod",
                    "fugiat",
                    "cupidatat",
                    "in"
                ],
                "friends": [
                    {
                        "id": 0,
                        "name": "Joyce Barry"
                    },
                    {
                        "id": 1,
                        "name": "Jeanette Pate"
                    },
                    {
                        "id": 2,
                        "name": "Allison Conley"
                    }
                    ],
                        "greeting": "Hello, Mack Larsen! You have 9 unread messages.",
                        "favoriteFruit": "apple"
                    }
        ]
        resp.body = json.dumps(quotes)

 
api = falcon.API()
api.add_route('/quote', QuoteResource())
api.add_route('/quotes', QuotesResource())
