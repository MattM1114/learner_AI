const wrapper = document.querySelector('.wrapper');
const registerlink = document.querySelector('.register-link');
const loginlink = document.querySelector('.login-link');

registerlink.onclick = () =>{
    wrapper.classlist.add('active');
}

loginlink.onclick = () =>{
    wrapper.classlist.remove('active');
}