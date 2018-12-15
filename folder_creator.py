import os
path = os.getcwd()
print("Welcome to Folder Creator v1.0")
print("Created by @mrOmotola")
name = input("Enter the name of your folder:")
def create(name):
    print("Pick a type of folder/file")
    print("1. Web Development Folder")
    print("2. Normal Folder")
    type = int(input("Enter a number: "))
    if type == 1 :
        print("Pick scripting language")
        print("1. Normal HTML folder")
        print("2. PHP folder")
        print("3. NodeJS folder")
        print("4. Python folder")
        web = int(input("Enter a number: "))
        if web == 1:
            try:
                os.mkdir(name)
                os.chdir(name)
                f = open("index.html", "w+")
                content = """<!DOCTYPE html>
                <html>
                <head>
                <title></title>
                <link rel='stylesheet' type='text/css' href='style.css'>
                <script type='text/javascript' src='style.js'></script>
                </head>
                <body></body>
                </html>"""
                f.write(content)
                f.close()
                f = open("style.css", "w+")
                content = "body{ padding: 0; margin: 0; font: Arial; color: black; }"
                f.write(content)
                f.close()
                f = open("script.js", "w+")
                content = ""
                f.write(content)
                f.close
            except FileExistsError:
                print("Folder already exists")
            except OSError:
                print ("Folder creation failed")
            else:
                print ("Folder creation successful. Thank you for creating your folder with @mrOmotola's folder creator.")
        elif web == 2:
            try:
                os.mkdir(name)
                os.chdir(name)
                f = open("index.php", "w+")
                content = """<?php ?>
                <!DOCTYPE html>
                <html>
                <head>
                <title></title>
                <link rel='stylesheet' type='text/css' href='style.css'>
                <script type='text/javascript' src='style.js'></script>
                </head>
                <body></body>
                </html>"""
                f.write(content)
                f.close()
                f = open("style.css", "w+")
                content = "body{ padding: 0; margin: 0; font: Arial; color: black; }"
                f.write(content)
                f.close()
                f = open("script.js", "w+")
                content = ""
                f.write(content)
                f.close
            except FileExistsError:
                print("Folder already exists")
            except OSError:
                print ("Folder creation failed")
            else:
                print ("Folder creation successful. Thank you for creating your folder with @mrOmotola's folder creator.")
        elif web == 3:
            try:
                os.mkdir(name)
                os.chdir(name)
                f = open("index.html", "w+")
                content = """
                <!DOCTYPE html>
                <html>
                <head>
                <title></title>
                <link rel='stylesheet' type='text/css' href='style.css'>
                <script type='text/javascript' src='style.js'></script>
                </head>
                <body></body>
                </html>"""
                f.write(content)
                f.close()
                f = open("style.css", "w+")
                content = "body{ padding: 0; margin: 0; font: Arial; color: black; }"
                f.write(content)
                f.close()
                f = open("server.js", "w+")
                content = """
                var http = require('http');
                var url = require('url');
                var fs = require('fs');
                http.createServer(function (req, res) {
    var q = url.parse(req.url, true);
    if(req.url == "/"){
        fs.readFile("index.html", function(err, data) {
        if (err) {
        res.writeHead(404, {'Content-Type': 'text/html'});
        return res.end("404 Not Found");
        }  
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(data);
        return res.end();
    });
    }
    var filename = "." + q.pathname;
    fs.readFile(filename, function(err, data) {
        if (err) {
        res.writeHead(404, {'Content-Type': 'text/html'});
        return res.end("404 Not Found");
        }  
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(data);
        return res.end();
    });
    }).listen(8080);"""
                f.write(content)
                f.close
            except FileExistsError:
                print("Folder already exists")
            except OSError:
                print ("Folder creation failed")
            else:
                print ("Folder creation successful. Thank you for creating your folder with @mrOmotola's folder creator.")
        elif web == 4:
            try:
                os.mkdir(name)
                os.chdir(name)
                f = open("index.pih", "w+")
                content = """<% %>
                <!DOCTYPE html>
                <html>
                <head>
                <title></title>
                <link rel='stylesheet' type='text/css' href='style.css'>
                <script type='text/javascript' src='style.js'></script>
                </head>
                <body></body>
                </html>"""
                f.write(content)
                f.close()
                f = open("style.css", "w+")
                content = "body{ padding: 0; margin: 0; font: Arial; color: black; }"
                f.write(content)
                f.close()
                f = open("script.js", "w+")
                content = ""
                f.write(content)
                f.close
            except FileExistsError:
                print("Folder already exists")
            except OSError:
                print ("Folder creation failed")
            else:
                print ("Folder creation successful. Thank you for creating your folder with @mrOmotola's folder creator.")
    elif type == 2:
        try:
            os.mkdir(name)
        except FileExistsError:
                print("Folder already exists")
        except OSError:
                print ("Folder creation failed")
        else:
                print ("Folder creation successful. Thank you for creating your folder with @mrOmotola's folder creator.")
create(name)