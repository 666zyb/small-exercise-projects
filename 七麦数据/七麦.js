function p(t) {
    t = encodeURIComponent(t)["replace"](/%([0-9A-F]{2})/g, function (n, t) {
        return o('0x' + t)
    });
    return btoa(t)
}

function h(n, t) {
    t = t || u();
    for (var e = (n = n["split"](""))["length"], r = t["length"], a = "charCodeAt", i = 0; i < e; i++)
        n[i] = o(n[i][a](0) ^ t[(i + 10) % r][a](0));
    return n['join']("")
}

function o(n) {
    t = "",
        ['66', '72', '6f', '6d', '43', '68', '61', '72', '43', '6f', '64', '65']["forEach"](function (n) {
            t += unescape("%u00" + n)
        });
    var t, e = t;
    return String[e](n)
}

a=[0,"6014"]
function zyb(a){
    a=a["sort"]()["join"]("")
    r = +new Date() - (732 || 0) - 1661224081041
    a=p(a)
    a=(a += "@#" + '/indexV2/getIndexRank') + ("@#" + r) + ("@#"+ 3)

    d = "xyz517cda96efgh";

    e = p(h(a, d))
    return e
    // console.log(e)
}
