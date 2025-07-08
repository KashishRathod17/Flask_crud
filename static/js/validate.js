function setupValidation(formSelector) {
    $(formSelector).validate({
        rules: {
            name: {
                required: true,
                minlength: 2
            },
            email: {
                required: true,
                email: true
            },
            p_no: {
                required: true,
                digits: true,
                minlength: 10,
                maxlength: 15
            },
            b_date: {
                required: true,
                date: true
            }
        },
        messages: {
            name: {
                required: "Please enter your name",
                minlength: "Name must be at least 2 characters"
            },
            email: {
                required: "Please enter your email",
                email: "Enter a valid email"
            },
            p_no: {
                required: "Please enter your phone number",
                digits: "Only numbers allowed",
                minlength: "Phone number must be at least 10 digits",
                maxlength: "Phone number must not exceed 15 digits"
            },
            b_date: {
                required: "Please select your birth date"
            }
        }
    });
}
