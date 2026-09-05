main_cities = ["Tokyo", "Kyoto", "Osaka", "Hakone", "Nara", "Hiroshima", "Kanazawa"]
food = ["katsu", "sushi", "ramen", "curry", "ice cream"]
shrines = ["asakusa", "hanazono", "shibuya", "meiji"]

#list of potential destinations:
#coffee shops
#pastry shops
#general eateries
#shrines
#temples
#hotels
#subway & train stations
#hotels
#onsen & sento - tattoo friendly
#sanrio stores
#public restrooms
#konbinis
#theme parks
#government buildings
#vending machines??
#not technically a place but data that will tell you WHICH FLOOR SOMETHING IS ON
#pokemon centers - is this technically a theme park??
#airports
#exhibitions - ie hello kitty in kyoto
#gardens?? ie murinan
#landmarks ie shibuya crossing, tokyo tower etc.
#day spas - tattoo friendly
#tea houses
#museums
#laundromats
#gyms??


import random

cities = {
    "tokyo": {
        "prefecture": "tokyo",
        "region": "kantō",
        "neighborhoods": [
            "tokyo station & marunouchi",
            "nihonbashi",
            "ginza",
            "tsukiji",
            "yurakucho",
            "kanda",
            "akihabara",
            "ochanomizu",
            "asakusa",
            "ueno",
            "yanaka",
            "nezu",
            "sendagi",
            "ryogoku",
            "kinshicho",
            "oshiage & tokyo skytree",
            "kiyosumi-shirakawa",
            "monzen-nakacho",
            "toyosu",
            "odaiba",
            "shinjuku",
            "shin-okubo",
            "kagurazaka",
            "nakano",
            "koenji",
            "kichioji",
            "shibuya",
            "harajuku",
            "omotesando",
            "daikanyama",
            "ebisu",
            "shimokitazawa",
            "sangenjaya",
            "roppongi",
            "akasaka",
            "aoyama",
            "azabu",
            "toranomon",
            "shinagawa",
            "gotanda",
            "meguro",
            "jiyugaoka",
            "oimachi",
            "ota & haneda"
        ],
        "shrines": [
            "asakusa",
            "atago",
            "chinreisha",
            "fushimi sanpō inari",
            "hanazono",
            "hie",
            "hikawa",
            "kameido tenjin",
            "kanda",
            "karasumori",
            "kasai",
            "kume no heinai-dō",
            "maruyama",
            "meiji jingu",
            "mita hachiman",
            "musashino inari",
            "namiyoke inari",
            "nogi",
            "ōji",
            "ōkunitama",
            "ōmiya hachimangū",
            "ono",
            "shiba tōshō-gū",
            "shōin",
            "suga",
            "suitengū",
            "takanawa",
            "teppozu inari",
            "tōgō",
            "tokyo daijingu",
            "tomioka hachiman",
            "ueno tōshō-gū",
            "yabo tenmangū",
            "yasukuni",
            "yushima tenmangū"
        ],
        "train stations": {
            "JR": {
                "yamanote":[
                    "nippori",
                    "nishi-nippori",
                    "tabata",
                    "komagome",
                    "sugamo",
                    "otsuka",
                    "ikebukuro",
                    "mejiro",
                    "takadanobaba",
                    "shin-okubo",
                    "shinjuku",
                    "yoyogi",
                    "harajuku",
                    "shibuya",
                    "ebisu",
                    "meguro",
                    "gotanda",
                    "osaki",
                    "shinagawa",
                    "takanawa gateway station",
                    "tamachi",
                    "hamamatsucho",
                    "shimbashi",
                    "yurakucho",
                    "tokyo central station",
                    "kanda",
                    "akihabara",
                    "okachimachi",
                    "ueno",
                    "uguisudani"
                ]
            },
            "tokyo metro": {
                "ginza": [
                    "shibuya",
                    "omote-sando",
                    "gaiemmae",
                    "aoyama-itchome",
                    "akasaka-mitsuke",
                    "tameike-sanno",
                    "toranomon",
                    "shimbashi",
                    "ginza",
                    "kyobashi",
                    "nihombashi",
                    "mitsukoshimae",
                    "kanda",
                    "suehirocho",
                    "ueno hirokoji",
                    "ueno",
                    "inaricho",
                    "tawaramachi",
                    "asakusa"
                ]
            },
            "toei": {
                "oedo": [
                    "shinjuku-nishiguchi",
                    "higashi-shinjuku",
                    "wakamatsu-kawada",
                    "ushigome-yanagicho",
                    "ushigome-kagurazaka",
                    "iidabashi",
                    "kasuga",
                    "hongō-sanchōme",
                    "ueno-okachimachi",
                    "shin-okachimachi",
                    "kuramae",
                    "ryōgoku",
                    "morishita",
                    "kiyosumi-shirakawa",
                    "monzen-nakachō",
                    "tsukishima",
                    "kachidoki",
                    "tsukijishijō",
                    "shiodome",
                    "daimon",
                    "akabanebashi",
                    "azabu-juban",
                    "roppongi",
                    "aoyama-itchōme",
                    "kokuritsu-kyōgijō",
                    "yoyogi",
                    "shinjuku",
                    "tochōmae",
                    "nishi-shinjuku-gochōme",
                    "nakano-sakaue",
                    "higashi-nakano",
                    "nakai",
                    "ochiai-minami-nagasaki",
                    "shin-egota",
                    "nerima",
                    "toshimaen",
                    "nerima-kasugachō",
                    "hikarigaoka"
                ]
            },
        },
    },    
    "kyoto":{
        "prefecture": "kyoto",
        "region": "kansai",
        "neighborhoods": [
            "kyoto station",
            "downtown & shijo-kawaramachi",
            "karasuma",
            "shijo",
            "sanjo",
            "nishiki",
            "gion",
            "higashiyama",
            "kiyomizu",
            "okazaki",
            "philosopher's path",
            "nanzenji",
            "keage",
            "kitano",
            "kinugasa",
            "nishijin",
            "kurama",
            "kifune",
            "ohara",
            "takao",
            "arashiyama",
            "saga",
            "uzumasa",
            "katsura",
            "nishikyo",
            "fushimi",
            "inari",
            "tofukuji",
            "yamashina"
        ],
        "shrines": [
            "Fushimi Inari Taisha",
            "Yasaka-jinja",
            "Heian-jingu",
            "Kitano Tenmangu",
            "Shimogamo-jinja",
            "Kamigamo-jinja",
            "Kifune-jinja",
            "Yoshida-jinja",
            "Hirano-jinja",
            "Matsunoo-taisha",
            "Ōharano-jinja",
            "Umenomiya-taisha",
            "Imamiya-jinja",
            "Seimei-jinja",
            "Shiramine-jingu",
            "Mikane-jinja",
            "Kyoto Kumano-jinja",
            "Kumano Nyakuōji-jinja",
            "Okazaki-jinja",
            "Awata-jinja",
            "Toyokuni-jinja",
            "Fujinomori-jinja",
            "Gokōnomiya-jinja",
            "Rokusonno-jinja",
            "Kisshōin Tenmangū",
            "Saion Kasuga-jinja",
            "Nagaoka Tenmangū",
            "Waratenjin-gū",
            "Goryō-jinja",
            "Sugawara-in Tenmangū",
            "Ichihime-jinja",
            "Jōnangū",
            "Kyoto Ryozen Gokoku-jinja",
            "Kyoto Ebisu-jinja",
            "Yuki-jinja",
            "Matsugasaki-jinja",
            "Goō-jinja",
            "Kenkun-jinja",
            "Tōgō-jinja"
        ],
        "train stations": {
            "kyoto city subway": {
                "karasuma line": [
                    "kokusaikaikan",
                    "matsugasaki",
                    "kitayama",
                    "kitaōji", #good for daitoku-ji temple
                    "kuramaguchi",
                    "imadegawa", #good for kyoto imperial palace
                    "marutamachi",
                    "karasuma oike", #interchange w tozai line
                    "shijō", #connects to hankyu kyoto line @ karasuma station
                    "gojō",
                    "kyōto", #connects to JR lines & shinkansen
                    "kujō",
                    "jūjō",
                    "kuinabashi",
                    "takeda" #connects to kintetsu kyoto line
                ],
                "tozai line": [
                    "rokujizo",
                    "ishida",
                    "daigo", #good for daigoji temple
                    "ono",
                    "nagitsuji",
                    "higashino",
                    "yamashina",
                    "misasagi",
                    "keage", #for nanzenji
                    "higashiyama", #for okazaki museum district
                    "sanjo keihan station", #transfer to keihan line
                    "kyoto shiyakusho-mae", # city hall
                    "karasuma oike", #transfer to karasuma line
                    "nijojo-mae", #for nijo castle
                    "nijo",
                    "nishioji oike",
                    "uzumasa tenjingawa station"
                ]
            },
            "JR": {
                "sagano line": [
                    "kyoto",
                    "umekoji-kyotonishi",
                    "tambaguchi",
                    "nijo", #access to nijo castle
                    "emmachi",
                    "hanazono",
                    "uzumasa", #access to toei kyoto studio park
                    "saga-arashiyama", #access to arashiyama bamboo grove
                    "hozukyo",
                    "umahori",
                    "kameoka",
                    "namiki",
                    "chiyokawa",
                    "hagiwara",
                    "sonobe" #end terminal for sagano line commuter service
                ]
            },
        },
    },    
    "osaka": {
        "prefecture": "osaka",
        "region": "kansai",
        "neighborhoods": [
            "umeda",
            "kita",
            "nakazaki-cho",
            "tenjinbashisuji",
            "fukushima",
            "nakanoshima",
            "honmachi",
            "yodoyabashi",
            "kitahama",
            "shinsaibashi",
            "amerikamura",
            "horie",
            "namba",
            "dotonbori",
            "nipponbashi",
            "kuromon",
            "tennoji",
            "abenobashi",
            "shitennoji",
            "shinsekai",
            "tsutenkaku",
            "bay area",
            "osaka bay",
            "tempozan",
            "universal city",
            "osaka castle",
            "kyobashi",
            "tanimachi",
            "tenma",
            "taisho",
            "sumiyoshi",
            "sakai"
        ],
        "shrines": [
            "Sumiyoshi Taisha",
            "Ikukunitama Shrine",
            "Osaka Tenmangu",
            "Imamiya Ebisu Shrine",
            "Horikoshi Shrine",
            "Tsuyuten Shrine",
            "Horikawa Ebisu Shrine",
            "Ikasuri Shrine",
            "Sukunahikona Shrine",
            "Goryo Shrine",
            "Toyokuni Shrine",
            "Tamatsukuri Inari Shrine",
            "Takatsu Shrine",
            "Sanko Shrine",
            "Kumata Shrine",
            "Abeno Oji Shrine",
            "Abe no Seimei Shrine",
            "Yasui Shrine",
            "Yodogawa Shrine",
            "Kitsuki Shrine",
            "Kashiwara Shrine",
            "Yae Shrine",
            "Ikune Shrine",
            "Nozato Sumiyoshi Shrine",
            "Kanda Tenmangu Shrine",
            "Kayashima Shrine",
            "Hyotanyama Inari Shrine",
            "Otori Taisha",
            "Mozu Hachiman Shrine",
            "Hagiwara Tenjin"
        ],
        "train stations": {
            "osaka metro": {
                "midosuji line": [
                    "esaka",
                    "higashimikuni",
                    "shin-osaka",
                    "nishinakajima-minamigata",
                    "nakatsu",
                    "umeda",
                    "yodoyabashi",
                    "honmachi",
                    "shinsaibashi",
                    "namba",
                    "daikokucho",
                    "dobutsuen-mae",
                    "tennoji",
                    "showacho",
                    "nishitanabe",
                    "nagai",
                    "abiko",
                    "kitahanada",
                    "shinkanaoka",
                    "nakamozu"
                ],
                "chuo line": [
                    "yumeshima",
                    "cosmo square", #transfer to new tram
                    "osakako", #near osaka aquarium
                    "asashiobashi", #near yahataya park
                    "bentencho", #transfer to osaka loop line
                    "kujo", #transfer to hanshin namba line
                    "awaza", #transfer to sennichimae line
                    "hommachi", #transfer to midosujui & yotsubashi lines
                    "sakaisuji-hommachi", #transfer to sakaisuji line
                    "tanimachi 4-chome", #transfer to tanimachi line, near osaka castle
                    "morinomiya",#transfer to osaka loop line & nagahori tsurimi-ryokuchi line
                    "midoribashi", #transfer to imazatosuji line
                    "fukaebashi"
                    "takaida", #near takaida-chuo station for JR osaka higashi line
                    "nagata", #connects to kintetsu keihanna line
                ],
                "tanimachi line": [
                    "dainichi",
                    "moriguchi",
                    "taishibashi-imaichi",
                    "sembayashi-omiya",
                    "sekime-takadono",
                    "noe-uchindai",
                    "miyakojima",
                    "tenjimbashisuji 6-chome",
                    "nakazakicho",
                    "higashi-umeda",
                    "minamimorimachi",
                    "temmabashi",
                    "tanimachi 4-chome",
                    "tanimachi 6-chome",
                    "tanimachi 9-chome",
                    "shitennoji-mae yuhigaoka",
                    "tennoji",
                    "abeno",
                    "fuminosato",
                    "tanabe",
                    "komagawa-nakano",
                    "hirano",
                    "kire-uriwari",
                    "deto",
                    "nagahara",
                    "yao-minami"
                ],
                "sakaisuji line": [
                    "tenjimbashisuji 6-chome",
                    "ogimachi",
                    "minami-morimachi",
                    "kitahama",
                    "sakaisuji-hommachi",
                    "nagahoribashi",
                    "nippombashi",
                    "ebisucho",
                    "dobutsuen-mae",
                    "tengachaya"
                ]
            },
            "JR": {
                "osaka loop line": [
                    "osaka", #major transit & shopping hub
                    "fukushima", #dining & nightlife district
                    "noda", #quiet residential area
                    "nishikujō", #connection for universal studios (yumesaki line)
                    "bentencho", #transfer to osaka metro chuo line
                    "taishō", #connection to nagahori tsurumi-ryokuchi line
                    "ashiharabashi",
                    "imamiya", #transfer to yamatoji line
                    "shin-imamiya", #major transfer hub for nankai & yamatoji lines
                    "tennōji", #near tennoji park & abeno harukas
                    "teradachō", 
                    "momodani",
                    "tsuruhashi", #famous for korean town & bbq restaurants
                    "tamatsukuri", #transfer to nagahori tsurumi-ryokuchi line
                    "morinomiya", #walking access to osaka castle park
                    "osakajō-koen", #right next to osaka castle
                    "kyōbashi", #commercial & entertainment district
                    "sakuranomiya", #scenic riverside park area
                    "temma" #home to japan's longest shopping arcade
                ],
                "yumesaki line": [
                    "nishikujo",
                    "ajikawaguchi",
                    "universal-city",
                    "sakurajima"
                ]
            },
        },
    },    
    "nara": {
        "prefecture": "nara",
        "region": "kansai",
        "neighborhoods": [
            "nara station",
            "naramachi",
            "nara park",
            "sanjo-dori",
            "higashimuki",
            "mochidonō",
            "gioncho",
            "takabatake",
            "kasugano",
            "higashiyama",
            "nishinokyo",
            "saidaiji",
            "heijo palace",
            "saho",
            "mihoyama",
            "hannyaji",
            "shibatsuji",
            "omiya",
            "kyobate",
            "narahama"
        ],
        "shrines": [
            "Kasuga Taisha",
            "Himuro Shrine",
            "Tamukeyama Hachimangu",
            "Nara-ken Gokoku Shrine",
            "Saho Shrine",
            "Mikasa Shrine",
            "Hirano Shrine",
            "Mizutani Shrine",
            "Tatsuta Shrine",
            "Naramachi Tenjinsha",
            "Nara City Sugawara Shrine",
            "Kaidan-in Hachimangu",
            "Yatagarasu Shrine"
        ],
        "train stations": {
            "JR": {
                "yamatoji line": [
                    "nara",
                    "koriyama",
                    "yamato-koizumi",
                    "horyuji",
                    "sango",
                    "oji", #major transfer station
                    "kawachi-katakami",
                    "takaida",
                    "kashiwara",
                    "shiki",
                    "yao",
                    "kyuhoji",
                    "kami",
                    "hirano",
                    "tobushijomae",
                    "tennoji",
                    "shin-imamiya",
                    "imamiya",
                    "JR Namba"
                ],
                "nara line": [
                    "kyoto", #connects to shinkansen & main JR lines
                    "tōfukuji", #transfer to keihan main line
                    "inari", #closest stop to fushimi inari shrine
                    "JR fujinomori",
                    "uji", #famous for byōdō-in temple
                    "kizu", #trains merge into yamatoji line here
                    "nara"
                ],
                "sakurai line": [ #aka manyo mahoroba line
                    "nara", #transfers to yamatoji, kansai lines
                    "kyobate",
                    "obitoke",
                    "ichinomoto",
                    "tenri", #transfers to kintetsu tenri line
                    "nagara",
                    "yanagimoto",
                    "makimuku",
                    "miwa",
                    "sakurai", #transfers to kintetsu osaka line
                    "kaguyama",
                    "unebi",
                    "kanahashi",
                    "takada" #transfers to JR wakayama line
                ]
            },
            "kintetsu": {
                "kyoto line": [
                    "kyoto",
                    "tōji",
                    "jūjō",
                    "rakusaiguchi",
                    "takeda", #connects w kyoto municipal subway karasuma line
                    "fushimi",
                    "kintetsu-tamba-bashi",
                    "momoyama-goryō-mae",
                    "mukajima",
                    "ogura",
                    "iseda",
                    "ōkubo",
                    "kutsuwa",
                    "tonoshō",
                    "shin-hōsono",
                    "kintetsu-miyazu",
                    "komada",
                    "shin-tanabe",
                    "kōdo",
                    "miyamaki",
                    "kintetsu-gakkenmae",
                    "hiragino",
                    "yamato-saidaiji", #junction for kintetsu nara line
                    "shin-omiya", #kintetsu nara line portion
                    "kintetsu-nara"
                ],
                "kashihara line": [
                    "yamato-saidaiji", #transfers to kyoto & nara lines
                    "amagatsuji",
                    "nishinokyō",
                    "kujō",
                    "kintetsu-kōriyama",
                    "tsutsui",
                    "hirahata", #transfer to tenri line
                    "family-kōemmae",
                    "yūzaki",
                    "iwami",
                    "tawaramoto", #transfer to tawaramoto line @ nishi-tawaramoto
                    "kasanui",
                    "ninokuchi",
                    "yamato-yagi", #transfer to osaka line
                    "yagi-nishiguchi",
                    "unebigoryōmae",
                    "kashiharajingū-mae"
                ],
                 "namba line": [
                    "osaka-namba", #transfer to hanshin namba line, osaka metro
                    "kintetsu-nippombashi", #transfer to osaka metro
                    "osaka-uehommachi", #transfer to kintetsu osaka line
                    "tsuruhashi", #transfer to osaka loop line, osaka metro
                    "imazato",
                    "fuse" #official end of namba line, becomes nara line
                ],
    # trains commonly operate through from the namba line
    # to the nara line without requiring a transfer at fuse
                "nara line": [
                    "fuse", #official start of nara line, connects to osaka/namba line
                    "kawachi-eiwa",
                    "kawachi-kosaka",
                    "yaenosato",
                    "wakae-iwata",
                    "kawachi-hanazono",
                    "higashi-hanazono",
                    "hyotan-yama",
                    "hiraoka",
                    "nukata",
                    "ishikiri",
                    "ikoma",
                    "higashi-ikoma",
                    "tomio",
                    "gakuemmae",
                    "ayameike",
                    "yamato-saidaiji",
                    "shin-omiya",
                    "kintetsu-nara"
                ]
            },
        },
    },    
    "hakone": {
        "prefecture": "kanagawa",
        "region": "kantō",
        "neighborhoods": [
            "hakone-yumoto",
            "tonosawa",
            "hatajuku",
            "ohiradai",
            "miyanoshita",
            "kowakudani",
            "gora",
            "miyagino",
            "kiga",
            "sengokuhara",
            "owakudani",
            "togendai",
            "motohakone",
            "hakonemachi",
            "ashinoyu",
            "hakone-en"
        ],
        "shrines": [
            "Hakone Shrine",
            "Kuzuryu Shrine",
            "Hakone Mototsumiya",
            "Kintoki Shrine",
            "Sengokuhara Suwa Shrine",
            "Shirayama Shrine",
            "Fukazawa Zeniarai Benzaiten",
            "Komagata Shrine",
            "Hakuryu Shrine"
        ],
        "train stations": {
            "hakone tozan railway": [
                "hakone-yumoto",
                "tonosawa",
                "ohiradai",
                "miyanoshita",
                "kowakudani",
                "chokoku-no-mori",
                "gora"
            ]
        },
    },                                            
},



welcome_msg = print("welcome to ikisaki torii!!\n")

# to be turned into functions:
# 1. sort by category or destination & view corresponding data
# 2. choose where to go or randomize

def select_destination():
    where = input("choose your destination or say 'surprise me'.\n").lower()
    random_city = random.choice(main_cities)
    if where == "surprise me":
        print(f"let's explore {random_city}")
    elif where in cities:
        print(f"welcome to {where}")
    else:
        print("sorry, that city is not currently supported. try again!!")

def select_category():
    choice = (input("which category would you like to view?\ntype destinations, food, or shrines\n")).lower()
    if choice == "destinations":
        print(main_cities)
    elif choice == "food":
        print(food)
    elif choice == "shrines":
        print(shrines)
    else:
        print("sorry, that category is not supported at this time. try again!!")    

select_destination()
select_category()
