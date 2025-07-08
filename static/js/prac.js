let dataTableInstance;
$(document).ready(function () {
  fetchUsers();
  function fetchUsers() {
    $.ajax({
      url: "/api/getalluser",
      type: "GET",
      dataType: "json",
      success: function (data) {
        if ($.fn.DataTable.isDataTable("#myDataTable")) {
          dataTableInstance.destroy();
        }
        $("#userTableBody").empty();
        $.each(data, function (index, user) {
          $("#userTableBody").append(
            `<tr>
                                <td>${index + 1}</td>
                                <td>${user.name}</td>
                                <td>${user.email}</td>
                                <td>${user.p_no}</td>
                                <td>${user.b_date}</td>
                                <td>
                                    <button id="updatebtn" class="btn btn-outline-dark mx-2" data-id="${
                                      user.u_id
                                    }">Update</button>
                                    <button id="deletebtn" class="btn btn-outline-dark" data-id="${
                                      user.u_id
                                    }">Delete</button>
                                </td>
                            </tr>`
          );
        });

        dataTableInstance = $("#myDataTable").DataTable();
      },
      error: function (error) {
        console.error("Error fetching users:", error);
      },
    });
  }

  // Add jQuery validation rules
  $("#userForm").validate({
    rules: {
      name: {
        required: true,
        minlength: 2,
      },
      email: {
        required: true,
        email: true,
      },
      p_no: {
        required: true,
        digits: true,
        minlength: 10,
        maxlength: 15,
      },
      b_date: {
        required: true,
        date: true,
      },
    },
    messages: {
      name: {
        required: "Please enter your name",
        minlength: "Name must be at least 2 characters",
      },
      email: {
        required: "Please enter your email",
        email: "Enter a valid email",
      },
      p_no: {
        required: "Please enter your phone number",
        digits: "Only numbers allowed",
        minlength: "Phone number must be at least 10 digits",
        maxlength: "Phone number must not exceed 15 digits",
      },
      b_date: {
        required: "Please select your birth date",
      },
    },
    submitHandler: function (form) {
      const formData = {
        name: $("#name").val(),
        email: $("#email").val(),
        p_no: $("#p_no").val(),
        b_date: $("#b_date").val(),
      };

      $.ajax({
        url: "/api/userjson",
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify(formData),
        success: function (response) {
          fetchUsers();
          $("#userForm")[0].reset();
          alert("User created successfully!");
        },
        error: function (xhr) {
          alert("Error: " + xhr.responseJSON.error);
          console.error(xhr.responseJSON);
        },
      });
    },
  });

  // Delete functionality
  $(document).on("click", "#deletebtn", function () {
    const u_id = $(this).data("id");
    if (confirm("Are you sure you want to delete this user?")) {
      $.ajax({
        url: `/api/apideleteuser/${u_id}`,
        type: "DELETE",
        success: function (response) {
          alert(response.message);
          fetchUsers();
        },
        error: function (xhr) {
          alert("Error deleting user: " + xhr.responseJSON.error);
          console.error(xhr.responseJSON);
        },
      });
    }
  });

  // Redirect to update page
  $(document).on("click", "#updatebtn", function () {
    const u_id = $(this).data("id");
    window.location.href = `/updateuser/${u_id}`;
  });
});
