import win32com.client, sys, MSO, MSPPT, MSPPTUtil
g = globals()
for c in dir(MSO.constants):    g[c] = getattr(MSO.constants, c)
for c in dir(MSPPT.constants):  g[c] = getattr(MSPPT.constants, c)
Application = win32com.client.Dispatch("PowerPoint.Application")

# Open PowerPoint
Application = win32com.client.Dispatch("PowerPoint.Application")
# Create new presentation
Presentation = Application.Presentations.Add()
# Add a blank slide
Slide = Presentation.Slides.Add(1, 12)


Presentation.save_as('C:\\Users\\ktl29155\\desktop\\exampleSlide.ppt')
 
Application.Quit()
