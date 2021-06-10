const btnDelete = document.querySelectorAll('.btn-delete')

if (btnDelete) {
    const btnArray = Array.from(btnDelete);

    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if (!confirm('Estas seguro de querer borrar el registro?')) {
                e.preventDefault();
            }
        });
    });
}

const currentLocation = location.href;
const menuItem = document.querySelectorAll('a');
const menuLenght = menuItem.length;
for (let i = 0; i < menuLenght; i++) {
    if (menuItem[i].href === currentLocation) {
        menuItem[i].className = "nav-link active"
    }
}
