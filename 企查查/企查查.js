var crypto = require('crypto-js')
window={
    tid:"c6104e71efbfd58afa93cd7039e2bc85",
    pid:"7507bb7e6de42ea9aaf3e6bd5c022ba5",
}

od1 = function () {
    codes = {
        "0": "W",
        "1": "l",
        "2": "k",
        "3": "B",
        "4": "Q",
        "5": "g",
        "6": "f",
        "7": "i",
        "8": "i",
        "9": "r",
        "10": "v",
        "11": "6",
        "12": "A",
        "13": "K",
        "14": "N",
        "15": "k",
        "16": "4",
        "17": "L",
        "18": "1",
        "19": "8"
    }
    for (var e = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase(), t = e + e, n = "", i = 0; i < t.length; ++i) {
        var o = t[i].charCodeAt() % 20;
        n += codes[o]
    }
    return n
}

ad1 = function (e, t) {
    return crypto.HmacSHA512(e, t).toString()
}

od = function () {
    var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
        , t = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
        , n = JSON.stringify(e).toLowerCase();
    return ad1(t + n, od1(t)).toLowerCase().substr(8, 20)
}

rd = function () {
    var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
        , t = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : ""
        , n = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
        , i = JSON.stringify(e).toLowerCase();
    return ad1(n + "pathString" + i + t,od1(n))
}

function sd() {
    var list = ["w", "i", "n", "d", "o", "w", ".", "t", "i", "d"];
    return eval(list.join(""))
}

function get_data(t) {
    e = {}
    t=t
    i = od(t, e.data)
    u = rd(t, e.data, sd());
    return {"i":i,"u":u}
}

get_data()