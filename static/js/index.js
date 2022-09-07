let editor;

window.onload = () => {
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/python");
    editor.find('needle',{
        backwards: false,
        wrap: false,
        caseSensitive: false,
        wholeWord: false,
        regExp: false
    });
    editor.findNext();
    editor.findPrevious();
    editor.setOptions({
        autoScrollEditorIntoView: true,
        copyWithEmptySelection: true,
    });
    editor.resize();
    document.getElementById('editor').style.fontSize='15px';
    editor.find('foo');
    editor.replace('bar');

}

function changeLangauge() {
    let lang = document.getElementById("lang");
    let langauge = lang.options[lang.selectedIndex].value;

    if (langauge=="c") 
        editor.session.setMode("ace/mode/c_cpp");
    else if(langauge=="cpp")
        editor.session.setMode("ace/mode/c_cpp");
    else if(langauge=="java")
        editor.session.setMode("ace/mode/java");
    else if(langauge=="js")
        editor.session.setMode("ace/mode/javascript");
    else
        // default python
        editor.session.setMode("ace/mode/python");
}

function excute(e) {
    let lang = document.getElementById("lang");
    let langauge = lang.options[lang.selectedIndex].value;
    let code = editor.getSession().getValue();
    let reqBody = {
        "langauge": langauge,
        "code": code
    }

    fetch("http://127.0.0.1:5000/", {
            method: "POST",
            headers: {
                "Content-Type" : "application/json",
            },
            body: JSON.stringify(reqBody)
        }).
        then(response => {
            return response.json()
        }).
        then(data => {
            console.log(data.output);
            let output = document.getElementById("output");
            output.innerHTML = data.output;
        }).
        catch(err => {
            let output = document.getElementById("output");
            output.innerHTML = "Please Try Later. Server Error :)"
        });
    
    return false;
}
