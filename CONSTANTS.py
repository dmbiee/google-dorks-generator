
#some constants and copy-paste variables
# |REPLACE| will be replaced by the func that uses it

SOCIAL_NETWORKS = " site:twitter.com OR site:facebook.com OR site:instagram.com OR site:tiktok.com OR site:youtube.com OR site:linkedin.com "

FILE_TYPES = " filetype:pdf OR filetype:doc OR filetype:docx "

GENERAL_SEARCH_LINKS_TEMPLATE = {
    "google_web" : "https://www.google.com/search?q=|REPLACE|",
    "googele_img":"https://www.google.com/search?q=|REPLACE|&udm=2",
    "bing_web":"https://www.bing.com/search?q=|REPLACE|",
    "bing_img":"https://www.bing.com/images/search?q=|REPLACE|&first=1",
    "yahoo":"https://search.yahoo.com/search?p=|REPLACE|",
    "yandex":"https://yandex.com/search/?text=|REPLACE|",
    "webmii":"https://webmii.com/people?n=|REPLACE|",
}

EMAIL_DOMAINS = [
    "@gmail.com",
    "@hotmail.com",
    "@hotmail.es",
    "@outlook.com",
    "@outlook.es",
    "@live.com",
    "@live.es",
    "@msn.com",
    "@yahoo.com",
    "@yahoo.es",
    "@icloud.com",
    "@me.com",
    "@protonmail.com",
    "@gmx.com",
    "@gmx.es",
    "@terra.es",
    "@terra.com",
    "@orange.es",
    "@telefonica.net",
    "@movistar.es",
    "@jazztel.es",
    "@euskalnet.net",
    "@ono.com",
    "@mail.com",
    "@aol.com  ",
]

# Mask for serching by username
USERNAME_MASK = [
    "|REPLACE|",
    "|REPLACE|1",
    "|REPLACE|123",
    "_|REPLACE|",
    "__|REPLACE|",
    "_|REPLACE|_",
    "|REPLACE|_",
    "|REPLACE|__",
    "0|REPLACE|",
    ".|REPLACE|",
    "|REPLACE|.",
    ".|REPLACE|."]
    
# Separators between FirstName and SecondName
SEPARATORS = [
        " ",
        ".",
        ", ",
        "_",
        "",]