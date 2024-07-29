var field = document.querySelectorAll('.forjs');
var nonfield = document.querySelectorAll('.nojs')
var enable_disable = document.querySelector('.enable-disable');


for (let index = 0; index < field.length; index++) {
    const element = field[index];
    element.setAttribute("disabled","disabled");
    element.style.cursor = 'default'
}

for (let index = 0; index < nonfield.length; index++) {
    const element = nonfield[index];
    element.setAttribute("disabled","disabled");
    element.style.cursor = 'default'
}


enable_disable.addEventListener('change',()=>{
    const enable_disabled = enable_disable.checked;
    for (let index = 0; index < field.length; index++) {
        const element = field[index];
        if (enable_disabled){
            element.removeAttribute("disabled");
            element.style.cursor = 'pointer'
        }
        else{
            element.setAttribute("disabled","disabled");
            element.style.cursor = 'default'
        }
    }
})

