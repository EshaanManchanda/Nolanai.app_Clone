from django.shortcuts import render
from .models import UserProfile,Scripts
import pandas as pd
# Create your views here.
import re
import json
import openai
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from typing import ContextManager
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.conf import settings
from django.db.models import Q
from django.contrib import messages
from .forms import ScriptForm
import json


import openai
from nolan import settings


# Create your views here.
def home(request):
    return render(request,'pages/index.html')
def about(request):
    return render(request,'pages/about.html')
def pricing(request):
    return render(request,'pages/pricing.html')
def for_studios(request):
    return render(request,'pages/for_studio.html')
def features(request):
    return render(request,'pages/features.html')
def blog(request):
    return render(request,'pages/blog.html')


#openai.organization = "org-chuck-norris-kernel"
openai.api_key = settings.ChatGPTKey



def Script(request):
  return render(request,"pages/Script.html")
def generate_script(title, plot):
    if openai.api_key == "":
        print("No API key.")
        return "No API key."

    script_metadata = ""
    script_metadata += f"Title: {title}\n\n"
    script_metadata += "Plot:\n"
    script_metadata += f"{plot}\n\n"

    request = """
    This is a script generation application.
    """ , script_metadata , """
    The script should contain 1 initial scenes and a list of characters.
    Do provide the complete dialogues and detailed descriptions and arrange them into specific the dictionary.
    Reply in json DiCTIONARY format: {
        "script": "Script content",
        "scene_headings":"List of all screen_headings used in the script in proper order",
        "dialogues":"List of all dialogues used in the script along with the charcters  speakking them",
        "scene_breakdown":"Scene breakdown based on scene headings that aligns the elements of 
        the above lists to make a scene making a proper arrangement of the action_lines list elements ,
        dialogues list elements ,and shots  list elements(Use list indexing along with the list names  only)",
        "shots ":"dictionary with scene_headings  as key and the shot as the value",
        "descriptive_lines":"List of all lines that dont fit into the above lists used in the script in proper order",
        "Characters": "List of characters"
    }
    The response should only contain this Dictionary.
    No part of the script should be left out of the dictionary
    you should use basic screenplay formatting.
    """
    print("IN GENERATE ", request)

    return query(request)

def query(request):
    # Call OpenAI API to generate the script
    #print("IN query")
    response = openai.Completion.create(
        engine="davinci-002",
        prompt=request,
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.2
    )
    #print(response)

    if response.choices:
        script = response.choices[1].text.strip().replace('\n', '\n\n')
        print("SCRIPT \n",response)
        return script
    else:
        #print("FAILED  FOR SOME REASONs", response.choices)
        return "Script generation failed."

#openai.api_key = "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"
# Create your views here.)
def GenerateSceen_play(form):
  print(form.cleaned_data['title'])
# def create_script(request):
#   form=ScriptForm()
#   return render(request,'pages/create_script.html',context={'form':form})

def create_script(request):
  if request.method=='POST':
    form = ScriptForm(request.POST)
    if form.is_valid():
      print("FORM IS VALID")
      title=form.cleaned_data['title']
      plot=form.cleaned_data['Plot']
      print(title , plot )
      DATA=generate_script(title, plot)
      DATA= DATA.replace("\n", " ").replace("  ", "")
      print(DATA)
      script = DATA
      return render(request,"pages/Script.html",{'form':form,'title':title,'plot':plot,'script':script})

  else:
    form = ScriptForm()
    print("Erros",form.errors)
  return render(request, "pages/create_script.html",context={'form':form})


# # Create your views here.
def get_characters_from_scene_heading(scene_heading):
    # Your logic to extract characters from a scene heading, modify as needed
    return ["Character1", "Character2"]

def get_shot_for_scene(scene_heading):
    # Your logic to determine the shot for a scene, modify as needed
    return "Wide Shot"

def create_scene_breakdown(script_dict):
    # Your logic to create a scene breakdown, modify as needed
    # This might involve aligning elements from scene_headings, dialogues, and shots
    return "Scene breakdown"