#set text(font: ("Noto Sans", "Liberation Sans", "DejaVu Sans"))
#set heading(numbering: "1.")
#show link: underline

// Set to true once the screenshots are in img/. While false, each
// screenshot is drawn as a labelled box so the PDF still builds.
#let screenshots = true

#let shot(path, caption) = figure(
  if screenshots {
    image(path, width: 40%)
  } else {
    rect(width: 90%, height: 4cm, stroke: (dash: "dashed"))[
      #align(center + horizon)[Screenshot: #raw(path)]
    ]
  },
  kind: image,
  caption: caption,
)

#align(center)[
  #text(size: 18pt, weight: "bold")[Earth Sciences Part II Computing]

  #text(size: 13pt)[Getting started]
]

= The course files

The file `python_course.zip` on Moodle contains all the files you need for
the course. Everything is also available on the #link("https://github.com/oscarbranson/esc_computing")[course GitHub repository].

Unzip it somewhere sensible, such as your Documents folder:
- *Windows:* right-click the file and choose _Extract All…_
- *macOS:* double-click the file.
- *Linux:* right-click the file and choose _Extract Here_, or run
  `unzip python_course.zip` in a terminal.

The exercises are #link("https://jupyter.org/")[Jupyter notebooks], which end in `.ipynb`. 
Keep the notebooks in the same folder as the `data` and `img` folders that come with them, because the notebooks load files from those folders.

= Setting up your computer

The course uses Python 3 and Jupyter notebooks. The first step of the course is getting your computer set up to run them.

There are few different ways to install Python and Jupyter.
For simplicity, we recommend using #link("https://www.anaconda.com/")[*Anaconda*] to install Python and the scientific packages we need, and #link("https://code.visualstudio.com/")[*VS Code*] to open and run the notebooks.
You are welcome to try other alternatives, but we can only promise to help with the Anaconda + VS Code setup.

This is worth setting up now. It's the same one you can use for Python in your project and beyond.

Allow about 30 minutes, most of it waiting for downloads. If you get stuck, see @troubleshooting, or ask in the first session.

== Install Anaconda

Download the Anaconda Distribution installer for your operating system from #link("https://www.anaconda.com/download")[anaconda.com/download]. 
You can skip the registration step.

- *Windows:* run the `.exe` installer. Choose _Just Me_, keep the suggested install location, and leave the advanced options at their defaults. In particular, leave _Add Anaconda to my PATH_ unticked.
- *macOS:* run the `.pkg` installer and accept the defaults. Choose the _Apple silicon_ installer for an M-series Mac, or the _Intel_ one for an older Mac.
- *Linux:* in a terminal, run `bash Anaconda3-<version>-Linux-x86_64.sh`. Accept the licence and the default location, and answer _yes_ when it asks whether to initialise conda. Then close and reopen the terminal.

== Install Cartopy

Two of the exercises use Cartopy to draw maps, and it doesn't come with Anaconda. Open a conda terminal:
- *Windows:* the _Anaconda Prompt_ app in the Start menu.
- *macOS and Linux:* the _Terminal_ app. 

The prompt (text on the left of a new line in the terminal) should contain `(base)`. If it doesn't, run `conda activate base` to switch to Anaconda's `base` environment.

Then run:

```bash
conda install cartopy
```

Answer `y` when it asks whether to proceed. If it asks you to accept Anaconda's Terms of Service, accept them and run the command again.

== Install VS Code

Download VS Code from #link("https://code.visualstudio.com/download")[code.visualstudio.com/download].

- *Windows:* run the _User Installer_ and accept the defaults.
- *macOS:* open the downloaded `.zip` and drag _Visual Studio Code_ into your _Applications_ folder.
- *Linux:* use your distribution's package manager (`apt`, `yum`, `pacman`, etc.).

== Add the Python and Jupyter extensions

Open VS Code and click the Extensions icon in the left-hand bar (`Ctrl`+`Shift`+`X`, or `Cmd`+`Shift`+`X` on macOS). Search for and install these two extensionst:
+ *Python*
+ *Jupyter*

#shot("img/vscode_extensions.png")[The Python and Jupyter extensions.]

== Open the course folder

Choose _File → Open Folder…_ (on macOS, _File → Open…_) and select the unzipped course folder. The Explorer on the left should show the `ExerciseN.ipynb` notebooks and the `data` and `img` folders.

VS Code will ask whether you trust the authors of the files in this folder.
Choose _Yes, I trust the authors_. Otherwise VS Code won't let you run any code.

== Choose the Python kernel

Open `Exercise0.ipynb` from the Explorer. The *kernel* is the Python that runs your code, and you need to tell VS Code to use Anaconda's:
+ Click _Select Kernel_ at the top right of the notebook.
+ Choose _Python Environments…_
+ Choose *base*, the one that mentions `anaconda3`.

The top right of the notebook should now show `base (Python 3.x.x)`. VS Code remembers this, but you may need to choose the kernel again the first time you open each notebook.

== Check that it works

Click _+ Code_ to add a code cell, type the line below into it, and press `Shift`+`Enter` to run it:

```python
import numpy, pandas, matplotlib, scipy, cartopy; print('All set!')
```

If it prints `All set!`, you're ready, and you can delete the cell again. Exercise 1 starts with a short tour of how notebooks work in VS Code.

= Troubleshooting <troubleshooting>

- *`base` isn't in the kernel list.* Close and reopen VS Code, then try again. If it's still missing, press `Ctrl`+`Shift`+`P` (`Cmd`+`Shift`+`P` on macOS), run _Python: Select Interpreter_, choose _Enter interpreter path…_ and browse to Anaconda's Python. On Windows that's `C:\Users\<you>\anaconda3\python.exe`. On macOS and Linux it's `~/anaconda3/bin/python`.

- *VS Code offers to install `ipykernel`.* You've chosen a Python that isn't Anaconda's. Choose the kernel again and pick *base*.

- *`ModuleNotFoundError: No module named 'cartopy'`.* Repeat the _Install Cartopy_ step above. Then click _Restart_ in the notebook's toolbar and run the cell again.

- *`FileNotFoundError` when loading data.* The notebook has been moved away from its `data` folder. Keep the notebooks where they were unzipped.

= Other ways to run the notebooks

You're welcome to use other tools, but the exercises assume VS Code, and we can only promise to help with the setup above.

- *JupyterLab* comes with Anaconda. Launch it from _Anaconda Navigator_.
- *#link("https://colab.research.google.com/")[Google Colab]* runs notebooks in your browser with your University Google account, and needs no installation. It may work, but it isn't supported. You'll need to upload the `data` and `img` folders as well as the notebooks, and run `!pip install cartopy` before the mapping exercises.
- Other editors, such as #link("https://www.jetbrains.com/pycharm/")[PyCharm], can also open notebooks.
