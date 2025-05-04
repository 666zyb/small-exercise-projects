

// 代理器封装


function get_enviroment(proxy_array) {
    for(var i=0; i<proxy_array.length; i++){
        handler = '{\n' +
            '    get: function(target, property, receiver) {\n' +
            '        console.log("方法:", "get  ", "对象:", ' +
            '"' + proxy_array[i] + '" ,' +
            '"  属性:", property, ' +
            '"  属性类型:", ' + 'typeof property, ' +
            // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof target[property]);\n' +
            '        return target[property];\n' +
            '    },\n' +
            '    set: function(target, property, value, receiver) {\n' +
            '        console.log("方法:", "set  ", "对象:", ' +
            '"' + proxy_array[i] + '" ,' +
            '"  属性:", property, ' +
            '"  属性类型:", ' + 'typeof property, ' +
            // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof target[property]);\n' +
            '        return Reflect.set(...arguments);\n' +
            '    }\n' +
            '}'
        eval('try{\n' + proxy_array[i] + ';\n'
        + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}catch (e) {\n' + proxy_array[i] + '={};\n'
        + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}')
    }
}
proxy_array = ['window', 'document', 'location', 'navigator', 'history','screen']

window = {}
window.parseInt = function (arg){}
window.reeseSkipExpirationCheck = true
window.reeseScriptLoadCount = 1
window.JSON = function (arg){
    return JSON.stringify(arg)
}
window.Array = function (arg){
    return  Array.from(arg)
}
window.RegExp = function (arg){
    return new RegExp(arg)
}
window.atob = function (arg){
    return atob(arg)
}
window.String = {
    fromCharCode: function (arg) {
        return String.fromCharCode(arg);
    },
}
window.navigator = {
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
,
}
window.fetch = function (arg) {
    console.log("fetch:"+"参数为:"+   arg)
}
get_enviroment(proxy_array)
document = {
    addEventListener: function (arg) {
        console.log(arg)
    },
    getElementsByTagName: function (arg) {
        console.log("document:"+"里的:"+ "getElementsByTagName"+"参数为:"+   arg)
        if (arg === "script") {
            return [script]
        }
    },
}
script = {
    src:'/rubie-Fease-no-sall-be-intome-Deat-seemselfe-Mot',
    type:"text/javascript",
    getAttribute :
    function (arg) {
        if (arg === 'src') {
            return script.src
        }
        }
}
location = {
    "ancestorOrigins": {},
    "href": "https://digital.etihad.com/book/cart-new/upsell/0/upsell",
    "origin": "https://digital.etihad.com",
    "protocol": "https:",
    "host": "digital.etihad.com",
    "hostname": "digital.etihad.com",
    "port": "",
    "pathname": "/book/cart-new/upsell/0/upsell",
    "search": "",
    "hash": ""
}
require('./0')
console.log(document.reese84)