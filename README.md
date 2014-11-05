# Django using jQuery File Upload Plugin
[jQuery-File-Upload](http://aquantum-demo.appspot.com/file-upload) was developed by Sebastian Tschan, with source on [github](https://github.com/blueimp/jQuery-File-Upload). 

This branch is an implementation of the same jQuery uploader using [Django 1.7](https://docs.djangoproject.com/en/1.7/) and [Python 2.7](https://docs.python.org/2/)
This branch also includes an implementation of [django-imagekit](http://django-imagekit.readthedocs.org/en/latest/) to generate thumbnails.

## Demo
[Demo File Upload](https://blueimp.github.io/jQuery-File-Upload/)

## Installation details
* Clone this repository
* run command 'python manage.py makemigrations'
* run command 'python manage.py migrate'
* run the server
* To test jquery file uploader, go to /upload/new/
* To test imagekit thumbnail generator and download previously uploaded images, go to /upload/view/
* To use Amazon s3 storage
    * Uncomment the configuration in imageUpload/settings.py
    * Add the access key and passwords
    * Uncomment the Media root and subroot

## Features
* **Multiple file upload:**  
  Allows to select multiple files at once and upload them simultaneously.
* **Drag & Drop support:**  
  Allows to upload files by dragging them from your desktop or filemanager and dropping them on your browser window.
* **Upload progress bar:**  
  Shows a progress bar indicating the upload progress for individual files and for all uploads combined.
* **Cancelable uploads:**  
  Individual file uploads can be canceled to stop the upload progress.
* **Resumable uploads:**  
  Aborted uploads can be resumed with browsers supporting the Blob API.
* **Chunked uploads:**  
  Large files can be uploaded in smaller chunks with browsers supporting the Blob API.
* **Client-side image resizing:**  
  Images can be automatically resized on client-side with browsers supporting the required JS APIs.
* **Preview images, audio and video:**  
  A preview of image, audio and video files can be displayed before uploading with browsers supporting the required APIs.
* **No browser plugins (e.g. Adobe Flash) required:**  
  The implementation is based on open standards like HTML5 and JavaScript and requires no additional browser plugins.
* **Graceful fallback for legacy browsers:**  
  Uploads files via XMLHttpRequests if supported and uses iframes as fallback for legacy browsers.
* **HTML file upload form fallback:**  
  Allows progressive enhancement by using a standard HTML file upload form as widget element.
* **Cross-site file uploads:**  
  Supports uploading files to a different domain with cross-site XMLHttpRequests or iframe redirects.
* **Multiple plugin instances:**  
  Allows to use multiple plugin instances on the same webpage.
* **Customizable and extensible:**  
  Provides an API to set individual options and define callBack methods for various upload events.
* **Multipart and file contents stream uploads:**  
  Files can be uploaded as standard "multipart/form-data" or file contents stream (HTTP PUT file upload).
* **Compatible with any server-side application platform:**  
  Works with any server-side platform (PHP, Python, Ruby on Rails, Java, Node.js, Go etc.) that supports standard HTML form file uploads.

## License
Released under the [MIT license](http://www.opensource.org/licenses/MIT).

### See Also
https://github.com/blueimp/jQuery-File-Upload/wiki#python
