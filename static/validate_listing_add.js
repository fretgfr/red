//price
//address_number
//address_zip
//bedrooms
//full_bathrooms
//half_bathrooms
//sqft
//year_built

//carcount
//acreage


//NOTE: This probably needs optimization seeing as I wrote this at 2 am
//and I'm tired.

function isNumInt(num) {
    return (!isNaN(parseInt(num)) && isFinite(num));
}

function isNumFloat(num) {
    return (!isNaN(parseFloat(num)) && isFinite(num));
}




const form = document.getElementById("add_listing");
form.addEventListener("submit", function (event) {

    let price = document.getElementById("price");
    let address_number = document.getElementById("address_number");
    let address_zip = document.getElementById("address_zip");
    let bedrooms = document.getElementById("bedrooms");
    let full_bathrooms = document.getElementById("full_bathrooms");
    let half_bathrooms = document.getElementById("half_bathrooms");
    let sqft = document.getElementById("sqft");
    let year_built = document.getElementById("year_built");
    let carcount = document.getElementById("carcount");
    let acreage = document.getElementById("acreage");

    let error = false;

    intval = [price, address_number, address_zip, bedrooms, full_bathrooms, half_bathrooms, sqft, year_built];

    floatval = [carcount, acreage];

    intval.forEach(function (val) {
        value = val.value;
        if (!isNumInt(value) || value < 0) {
            error = true;
            alert("Invalid entry for " + val.name);
        }
    });

    floatval.forEach(function (val) {
        value = val.value;
        if (!isNumFloat(value) || value < 0) {
            error = true;
            alert("Invalid entry for " + val.name);
        }
    });
    
    if (error) {
        event.preventDefault();
    }
});