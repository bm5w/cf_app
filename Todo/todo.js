function addItem()    {
    var x;
    var y;
    var text;

    // Get the value of the input field with id = "inputForm"
    x = document.getElementById("inputForm").value;

    //  NEED TO CHECK if item is in list already
    var elementExists = document.getElementById(x);
    if (elementExists == null)  {
        // Add item to list, with id the same as list
        var ul = document.getElementById("TheList");
        var li = document.createElement("li");
        li.appendChild(document.createTextNode(x));
        li.setAttribute("id",x);
        li.addEventListener("click", function(){var elem = document.getElementById(x);    elem.parentNode.removeChild(elem);});
        ul.appendChild(li);
    } else {
        alert("Item already in list!")
    }


}

function removal()    {
    var elem = document.getElementById(x)
    elem.parentNode.removeChild(elem)
    alert("test")

}