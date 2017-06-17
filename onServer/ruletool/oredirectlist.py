[
    {
        "name": "youkujson",
        "find": "https?:\/\/val[fcopb]\.atm\.youku\.com\/v[fcopb]",
        "replace": "about:blank",
        "extra": "adkillrule"
    },
    {
        "name": "youkuloader",
        "find": "https?:\/\/static\.youku\.com(\/v[\d\.]*)?\/v\/swf\/.*(\/)?loaders?\.swf",
        "exfind": "(bili|acfun)",
        "replace": "hostsite/loader.swf",
        "css": ".danmuoff .vpactionv5_iframe_wrap {top: auto !important;}",
        "extra": "adkillrule"
    },
    {
        "name": "youkuplayer",
        "find": "https?:\/\/static\.youku\.com(\/v[\d\.]*)?\/v\/swf\/.*(\/)?player.*\.swf",
        "exfind": "(bili|acfun)",
        "replace": "hostsite/player.swf",
        "css": ".danmuoff .vpactionv5_iframe_wrap {top: auto !important;}",
        "extra": "adkillrule"
    },
    {
        "name": "ku6",
        "find": "https?:\/\/player\.ku6cdn\.com\/default\/.*\/(v|player)\.swf",
        "replace": "hostsite/ku6.swf",
        "extra": "adkillrule"
    },
    {
        "name": "tudou",
        "find": "http:\/\/static\.youku\.com(\/v[\d\.]*)?\/v\/custom\/.*\/player.*\.swf",
        "exfind": "narutom",
        "replace": "hostsite/tudou.swf",
        "css": ".player {height: inherit !important;}",
        "extra": "adkillrule"
    },
    {
        "name": "tudou_olc",
        "find": "https?:\/\/js\.tudouui\.com\/.*olc[^\.]*\.swf",
        "replace": "hostsite/olc_8.swf",
        "extra": "adkillrule"
    },
    {
        "name": "tudou_sp",
        "find": "https?:\/\/js\.tudouui\.com\/.*SocialPlayer[^\.]*\.swf",
        "replace": "hostsite/sp.swf",
        "extra": "adkillrule"
    },
    {
        "name": "letvsdk",
        "find": "https?:\/\/player\.letvcdn\.com\/.*\/newplayer\/LetvPlayerSDK\.swf",
        "exfind": "(bili|acfun|com\/zt|duowan)",
        "replace": "hostsite/letvsdk.swf",
        "extra": "adkillrule"
    },
    {
        "name": "pplive",
        "find": "https?:\/\/player\.pplive\.cn\/ikan\/.*\/player4player2\.swf",
        "replace": "hostsite/player4player2.swf",
        "extra": "adkillrule"
    },
    {
        "name": "iqiyi",
        "find": "https?:\/\/www\.iqiyi\.com\/(player\/\d+\/Player|common\/flashplayer\/\d+\/((Main)?Player_.*|[\d]{4}[a-z]+((?!aa).){6,7}))\.swf",
        "exfind": "(baidu|61|178)\.iqiyi\.com|weibo|bilibili|acfun|(music|tieba)\.baidu",
        "replace": "hostsite/iqiyi5.swf",
        "extra": "adkillrule"
    },
    {
        "name": "pps",
        "find": "https?:\/\/www\.iqiyi\.com\/common\/.*\/pps[\w]+.swf",
        "replace": "hostsite/iqiyi_out.swf",
        "extra": "adkillrule"
    },
    {
        "name": "sohu_live",
        "find": "https?:\/\/(tv\.sohu\.com\/upload\/swf\/(p2p\/)?\d+|(\d+\.){3}\d+\/webplayer)\/Main\.swf",
        "exfind": "(bili|acfun)",
        "replace": "hostsite/sohu_live.swf",
        "extra": "adkillrule"
    },
    {
        "name": "duowan",
        "find": "https?:\/\/untitled\.dwstatic\.com\/.*",
        "replace": "about:blank",
        "extra": "adkillrule"
    }
]
