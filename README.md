# vscode-dynamic

Visual Studio Code, with a focus on dynamic languages.

## Requirements

* Visual Studio Code
* Node.js / NPM
* SQLite3
* PHP

## Python

### Virtual Environment

```bash
python3 -m venv 2_python_virt
```

```bash
cd 2_python_virt

source bin/activate
```

```bash
mkdir src

cd src

code .
```

Then, inside VS Code, create a new file "hello.py", and note the Python interpreter in use in the status line.

### Jupyter

In a VS Code project, right-click and create a file with a .ipynb extension.  VS Code will automatically create a Jupyter notebook.

### Django

```bash
python3 -m venv 3_django_test
```

```bash
cd 3_django_test

source bin/activate

code .
```

Inside VS Code:

* [F1], then
* Python: Select Interpreter

Select the interpreter in the virtual environment.

* [F1], then
* Terminal: Create New Terminal

```bash
pip install django
```

Create Django project:

```bash
django-admin startproject web_project .
```

Init SQLite database:

```bash
python manage.py migrate
```

Create an app:

```bash
python manage.py startapp hello
```

Modify hello/views.py as follows:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
```

Create hello/urls.py to set up a route:

```python
from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
]
```

Update web_project/urls.py to pull in the 'hello' routing configuration:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("hello.urls")),
    path('admin/', admin.site.urls)
]
```

Start the development server:

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser to see the output of the hello view.

## JavaScript / Node.js

```bash
mkdir node_hello

cd node_hello

code .
```

In VS Code:

1. New file...
2. app.js

Contents:

```javascript
var msg = 'Hello World';

console.log(msg);
```

Ways to run:

1. Open a new terminal and type `node app.js`, or
2. Press [F5].  You'll be prompted to use Node.js as your debugger.

Refactor the code to use a function:

```javascript
function say_hello(name) {
    console.log('Hello, ' + name);
}

say_hello('Jim');
```

Added a JSDoc comment:

```javascript
/** This function says hello! */
function say_hello(name) {
    console.log('Hello, ' + name);
}

say_hello('Jim');
```

When you hover over the call to `say_hello`, note the documentation text.

Set a breakpoint on the call to `say_hello`, press [F5], and step into the function to see the `msg` variable.

### TypeScript

```bash
mkdir ts_hello

cd ts_hello

npm install typescript --save-dev

code .
```

In VS Code, create a new file **helloworld.ts** with the following contents:

```typescript
let message: string = 'Hello World';

console.log(message);
```

To compile the TypeScript file, open the integrated terminal and run the TypeScript compiler:

```bash
npx tsc helloworld.ts
```

To control the TypeScript compiler, create a **tsconfig.json** file with the following contents:

```json
{
    "compilerOptions": {
        "target": "es5",
        "module": "commonjs",
        "outDir": "out"
    }
}
```

Now you can run `npx tsc` in the integrated terminal with no additional arguments.

To attach the debugger, add a source map option:

```json
{
    "compilerOptions": {
        "target": "es5",
        "module": "commonjs",
        "outDir": "out",
        "sourceMap": true
    }
}
```

With the **helloworld.ts** file open in the editor, you can now use [F5] to run and debug.  The first time you run, you'll be prompted for a debugger.  Select **Node**.

## Ruby

Ruby LSP configuration is being a pain, so we'll just use Code Runner for this.

## Perl

Open a terminal and install Perl::LanguageServer (required by the Perl extension):

```bash
sudo apt install libanyevent-perl libclass-refresh-perl libcompiler-lexer-perl \
libdata-dump-perl libio-aio-perl libjson-perl libmoose-perl libpadwalker-perl \
libscalar-list-utils-perl libcoro-perl
 
sudo cpan Perl::LanguageServer
```
