document.getElementById('get_file').onclick = function () {
    let form = document.querySelectorAll("#file_input");
    form[1].click();
};
// document.getElementById('get_file0').onclick = function () {
//     let form = document.querySelectorAll("#file_input");
//     form[0].click();
// };
// // document.getElementById('fileInput').addEventListener('change', function() {
// //     document.getElementById('buttom-submit').click();
// // });
// /*

// <!DOCTYPE html>
// <html lang="en">
// <head>
//     <meta charset="UTF-8">
//     <meta name="viewport" content="width=device-width, initial-scale=1.0">
//     <title>PDF Translator</title>
//     <style>
//         .dropzone {
//             width: 100%;
//             height: 200px;
//             border: 2px dashed #007bff;
//             display: flex;
//             align-items: center;
//             justify-content: center;
//             font-size: 18px;
//             color: #007bff;
//         }
//         .dropzone.dragover {
//             background-color: #e9ecef;
//         }
//     </style>
// </head>
// <body>
//     <h1>Upload and Translate PDF</h1>
//     <div class="dropzone" id="dropzone">
//         Drag and drop your PDF here
//     </div>
//     <input type="file" id="fileInput" style="display: none;">
//     <button id="uploadButton">Upload PDF</button>
//     <form id="uploadForm" enctype="multipart/form-data" style="display: none;">
//         <input type="hidden" name="csrfmiddlewaretoken" value="{{ csrf_token }}">
//         {{ form }}
//     </form>
//     <script>
        
//     </script>
// </body>
// </html>

// document.addEventListener('DOMContentLoaded', function () {
//             const dropzone = document.getElementById('dropzone');
//             const fileInput = document.getElementById('fileInput');
//             const uploadForm = document.getElementById('uploadForm');

//             dropzone.addEventListener('dragover', (e) => {
//                 e.preventDefault();
//                 dropzone.classList.add('dragover');
//             });

//             dropzone.addEventListener('dragleave', (e) => {
//                 dropzone.classList.remove('dragover');
//             });

//             dropzone.addEventListener('drop', (e) => {
//                 e.preventDefault();
//                 dropzone.classList.remove('dragover');
//                 fileInput.files = e.dataTransfer.files;
//             });

//             uploadButton.addEventListener('click', () => {
//                 if (fileInput.files.length > 0) {
//                     uploadFiles();
//                 } else {
//                     alert('Please select a file first.');
//                 }
//             });

//             function uploadFiles() {
//                 const formData = new FormData(uploadForm);
//                 formData.append('file', fileInput.files[0]);
//                 fetch('/upload/', {
//                     method: 'POST',
//                     body: formData,
//                     headers: {
//                         'X-CSRFToken': '{{ csrf_token }}'
//                     }
//                 })
//                 .then(response => response.json())
//                 .then(data => {
//                     if (data.message) {
//                         alert(data.message);
//                         window.location.href = data.translated_file;
//                     } else if (data.error) {
//                         alert(data.error);
//                     }
//                 })
//                 .catch(error => {
//                     console.error('Error:', error);
//                 });
//             }
//         });

// */