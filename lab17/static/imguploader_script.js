document.addEventListener("DOMContentLoaded", function () {
  const fileInput = document.getElementById("fileInput");
  const fileNameInput = document.getElementById("fileName");

  if (fileInput && fileNameInput) {
    fileInput.addEventListener("change", function () {
      fileNameInput.value =
        fileInput.files.length > 0 ? fileInput.files[0].name : "";
    });
  }

  const uploadForm = document.getElementById("uploadForm");
  if (uploadForm) {
    uploadForm.addEventListener("submit", function (e) {
      const file = fileInput.files[0];
      if (!file) {
        e.preventDefault();
        alert("Please select an image before uploading.");
      }
    });
  }
});
