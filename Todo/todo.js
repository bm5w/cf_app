function addItem()    {
    var x;
    var text;

    // Get the value of the input field with id = "inputForm"
    x = document.getElementById("inputForm").value;
    // Clear form after submit
    document.getElementById("inputForm").value=null;


    // Check if item is in list, add to list if not, alert if it is
    var elementExists = document.getElementById(x);
    if (elementExists == null)  {
        // Add item to list, with id the same as list
        var list = document.getElementById("TheList");
        var li = document.createElement("li");
        li.appendChild(document.createTextNode(x));
        li.setAttribute("id",x);
        li.addEventListener("click", function(){var elem = document.getElementById(x);    elem.parentNode.removeChild(elem);});
        //li.addEventListener("click", function(){document.getElementById("TheList").removeChild(elem);});
        list.insertBefore(li, list.childNodes[0]);
    } else {
        alert("Item already in list!")
    }
}