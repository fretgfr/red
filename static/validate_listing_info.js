/*
    Validates the listing data form to ensure that all of the passed in fields are valid.
*/


/* Decides whether a string represents a valid integer */
function isNumInt(num) {
    return (!isNaN(parseInt(num)) && isFinite(num));
}

/* Decides whether a string represents a valid floating point number */
function isNumFloat(num) {
    return (!isNaN(parseFloat(num)) && isFinite(num));
}

const form = document.getElementById("add_listing");
form.addEventListener("submit", function (event) { // Hook onto the submit event for the form and run the validation function

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
    let listagentid = document.getElementById("listing_agent_id");
    let colistagentid = document.getElementById("colist_agent_id");

    if (colistagentid.value == "") { // Default value for the co-listing agent.
        colistagentid.value = "0";
    }

    let error = false; // Flag to determine if the form can be submitted.

    // Integers that need validation.
    intval = [price, address_number, address_zip, bedrooms, full_bathrooms, half_bathrooms, carcount, sqft, year_built, listagentid, colistagentid];

    // Floats that need validation.
    floatval = [acreage];

    // Validate all integers.
    intval.forEach(function (val) {
        value = val.value;
        if (!isNumInt(value) || value < 0) {
            error = true; // Set error flag
            alert("Invalid entry for " + val.name);
        }
    });

    // Validate all floats.
    floatval.forEach(function (val) {
        value = val.value;
        if (!isNumFloat(value) || value < 0) {
            error = true; //Set error flag
            alert("Invalid entry for " + val.name);
        }
    });

    if (error) {
        event.preventDefault(); // Prevent the form from being submitted if there's an error.
    }
});