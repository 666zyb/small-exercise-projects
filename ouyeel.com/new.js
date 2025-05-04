function get_enviroment(proxy_array) {
    for (var i = 0; i < proxy_array.length; i++) {
        handler = '{\n' +
            '    get: function(target, property, receiver) {\n' +
            '        console.log("方法:", "get  ", "对象:", ' +
            '"' + proxy_array[i] + '" ,' +
            '"  属性:", property, ' +
            '"  属性类型:", ' + 'typeof property, ' +
            // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof target[property]);\n' +
            'if (typeof target[property] == "undefined"){debugger}' +
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

proxy_array = ['window', 'document', 'location', 'navigator', 'history', 'screen']


content = "content_code"

let log_flag = true

function vlog() {
    if (log_flag) {
        console.log(...arguments)
    }
}

_null = function () {
    vlog(arguments)
}
window = global
window.top = window
window.HTMLFormElement = _null
delete __filename;
delete __dirname;

div = {
    getElementsByTagName: function (arg) {
        if (arg === 'i') {
            return {length: 0}
        }
    },
}

scripy = {
    0: {},
    1: {}
}
meta = {
    getAttribute: function (arg) {
        if (arg === 'r') {
            return 'm'
        }
    },
    parentNode: {
        removeChild: _null
    }

}
document = {
    createElement: function (arg) {
        if (arg === 'div') {
            return div
        }
        if (arg === 'form') {
            return {}
        }
    },
    appendChild: _null,
    removeChild: _null,
    getElementById: _null,

    getElementsByTagName: function (arg) {
        vlog(arg)
        if (arg === 'script') {
            return scripy
        }
        if (arg === 'meta') {
            return [meta, meta]
        }
        if (arg === 'base') {
            return {}
        }
    }
}
location = {
    "ancestorOrigins": {},
    "href": "https://www.ouyeel.com/search-ng/queryResource/index",
    "origin": "https://www.ouyeel.com",
    "protocol": "https:",
    "host": "www.ouyeel.com",
    "hostname": "www.ouyeel.com",
    "port": "",
    "pathname": "/search-ng/queryResource/index",
    "search": "",
    "hash": ""
}
window.addEventListener = _null
setTimeout = _null
setInterval = _null

get_enviroment(proxy_array)


// require('./code')
'code'
require('./demo')
function getCookie() {
return document.cookie.split(';')[0]
}

console.log(getCookie());