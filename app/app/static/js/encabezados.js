const sizes = ['si', 'no'];

// generate the radio groups        
const group = document.querySelector(".group");
console.log(group)
group.innerHTML = sizes.map((size) => `<div>
        <input type="radio" name="size" value="${size}" id="${size}"+document.querySelector('.group').id>
            <label for="${size}">${size}</label>
    </div>`).join(' ');

// add an event listener for the change event
const radioButtons = document.querySelectorAll('input[name="size"]');
for(const radioButton of radioButtons){
    radioButton.addEventListener('change', showSelected);
}        

function showSelected(e) {
    console.log(e)
    num = 0;
    if (this.checked) {
        console.log(`#output${num}`)
        document.querySelector("#output").innerText = `You selected ${this.value}`;
        num++
    }
}