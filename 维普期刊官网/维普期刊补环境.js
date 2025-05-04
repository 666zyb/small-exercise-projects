delete __dirname
delete __filename

function get_enviroment(proxy_array) {
    for (var i = 0; i < proxy_array.length; i++) {
        handler = '{\n' + '    get: function(target, property, receiver) {\n' + '        console.log("方法:", "get  ", "对象:", ' + '"' + proxy_array[i] + '" ,' + '"  属性:", property, ' + '"  属性类型:", ' + 'typeof property, ' + // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof target[property]);\n' + '        return target[property];\n' + '    },\n' + '    set: function(target, property, value, receiver) {\n' + '        console.log("方法:", "set  ", "对象:", ' + '"' + proxy_array[i] + '" ,' + '"  属性:", property, ' + '"  属性类型:", ' + 'typeof property, ' + // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof target[property]);\n' + '        return Reflect.set(...arguments);\n' + '    }\n' + '}'
        eval('try{\n' + proxy_array[i] + ';\n' + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}catch (e) {\n' + proxy_array[i] + '={};\n' + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}')
    }
}

proxy_array = ['window', 'document', 'location', 'navigator', 'history', 'screen', 'aaa', 'target', 'localStorage']


window=global
delete buffer;
window.top=window
window.addEventListener=function (res,res1,res2){
    console.log("window中的addEventListener接收的值:",res,res1,res2)
}
window.attachEvent=function (res,res1){
    console.log("window中的attachEvent接收的值:",res,res1)
}

content1='meta-text'

meta=[
    {
        "http-equiv":"Content-Type",
        content:"text/html; charset=utf-8",
    },
    {
        id:"FbkwzLN5XOx0",
        content:content1,
        getAttribute:function (res){
            console.log("meta中的getAttribute接收的值:",res)
            if (res=='r'){
                return 'm'
            }
        },
        parentNode:{
            removeChild:function (res){
                console.log('meta中的removeChild接收的值:',res)
            }
        }
    }
]

div={
    getElementsByTagName:function (res){
        console.log('div中的getElementsByTagName接收的值:',res)
        if(res=='i'){
            return []
        }
    }
}

script={
    0:{
        type:"text/javascript",
        r:'m',
    },
    1:{
        type:"text/javascript",
        charset:"utf-8",
        src:"/N7xexRXkVdNQ/Y5oPTJBkyHck.cca831b.js",
        r:'m',
    }
}

document={
    createElement:function (res){
        console.log("document中的createElement接受的值:",res)
        if(res=='div'){
            return div
        }
    },
    getElementsByTagName:function (res){
        console.log("document中的getElementsByTagName接受的值:",res)
        if(res=='script'){
            return script
        }
        if (res=='base'){
            return []
        }
        if (res=='meta'){
            return meta
        }
    },
    getElementById:function (res){
        console.log("document中的getElementById接受的值:",res)
    },
    addEventListener:function (res){
        console.log("window中的addEventListener接收的值:",res)
    },
    attachEvent:function (res){
        console.log("window中的attachEvent接收的值:",res)
    }
}


location={
    "ancestorOrigins": {},
    "href": "https://qikan.cqvip.com/Qikan/Journal/JournalGuid?from=index",
    "origin": "https://qikan.cqvip.com",
    "protocol": "https:",
    "host": "qikan.cqvip.com",
    "hostname": "qikan.cqvip.com",
    "port": "",
    "pathname": "/Qikan/Journal/JournalGuid",
    "search": "?from=index",
    "hash": ""
}

setTimeout = function () {
}
setInterval = function () {
}


get_enviroment(proxy_array)

// require('./维普期刊cookie')

'html-code'

'ts-code'

function get_cookie(){
    return document.cookie
}

console.log(document.cookie)