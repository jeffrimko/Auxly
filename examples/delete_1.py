"""This example deletes all PYC files in the project."""
import auxly
import qprompt
delfunc = lambda is_test: auxly.filesys.delete("..", "\.pyc$", recurse=True, test=is_test)
delfiles = delfunc(True)
if len(delfiles):
    print("Files to delete:")
    print("\n".join(["    " + i for i in delfiles]))
    if qprompt.ask_yesno("OK to delete?"):
        if delfunc(False) == delfiles:
            qprompt.alert("Files deleted.")
        else:
            qprompt.warn("Some files not deleted!")
else:
    qprompt.alert("No files to delete.")
