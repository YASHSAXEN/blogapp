var comment_container = document.querySelector('.comment-add-container');
var comment_button = document.querySelector('.active');
var close = document.querySelector('.cancel');
var blog = document.querySelector('.blog');
var commnent = document.querySelector('.comments-container');
var codeblock = document.querySelectorAll('code');

codeblock.forEach((block)=>{
    var cpoy_el = document.createElement('div');
    cpoy_el.classList.add('copy')
    cpoy_el.textContent = 'Copy';
    block.prepend(cpoy_el);
    block.addEventListener('click',()=>{
            navigator.clipboard.writeText(block.textContent.slice(4));
            cpoy_el.textContent = 'Copied';
            setTimeout(()=>{
                cpoy_el.textContent = 'Copy';
            },2000)
    })
})

comment_button.addEventListener('click',()=>{
    blog.classList.add('notshow');
    commnent.classList.add('notshow');
    blog.classList.remove('remove');
    commnent.classList.remove('remove');
    comment_container.style.display = 'flex';
})

close.addEventListener('click',()=>{
    blog.classList.add('remove');
    commnent.classList.add('remove');
    blog.classList.remove('notshow');
    commnent.classList.remove('notshow');
    comment_container.style.display = 'none';
})
