The DevilBotz website is hosted on Github Pages (https://docs.github.com/en/pages), built by Jekyll using a fork of Jekyll-now repository by Barry Clark (https://github.com/barryclark/jekyll-now) that was built to help create blogging sites.

Members of the Business github group can edit and create blog entries for the new site. Here's quick instructions for doing it right here on GitHub:

1. Go to the 'blog' directory in the repository and open the 'blog-template.md' file. Copy all of the text there.
2. Go to the '_posts' directory and create a new file. Paste the blog template text.
3. Name the file in the format 'YYYY-MM-DD-[title of the blog post]', for example: 2022-02-12-jacks-coal-fired
4. Update all the top matter to match what you're creating. Don't change the 'layout' line. The category (for now) should just be the year. 
5. Change the Author line as appropriate.
6. Write your blog post using markdown format (https://www.markdownguide.org/cheat-sheet/).
7. You may include valid HTML in your post as well, but for most blogs, it shouldn't be needed.
8. Please start with an introductory paragraph before including any videos or images.
9. Commit your changes. Write a description of your blog post in the Commit message.
10. Have your post reviewed by a mentor. Make any changes requested.
11. **When it's all approved, add ".md" to the end of your file name.** Then **Commit changes** again.
10. After 5-10 minutes, check the /blog page and visit your post to make sure it looks the way you expect it to. If the post hasn't showed up, check the 'Actions' tab in the Repo to see if there was an error during the build.

## Assets
### Images
Most older website images are currently part of the devilbotz2876 repository. They should be hosted elsewhere, as this practice uses more filespace than free github pages are supposed to use.

For now, new images can be uploaded to the "Photos" directory for the applicable year (2024 Crescendo, currently). To add one to a blog post, follow these steps:
1. Open the image in your browser
2. Click the _Share_ button at top right and "Copy Link"
3. Paste the link into your story. It's temporary. It will look something like this:<br />```https://drive.google.com/file/d/11huaHsvkf38Zl7jVtOfqpCuUx4mb98BX/view?usp=sharing```<br />The part after the "/d/" and up to the next "/" is your image's ID.
- Paste the following into your story:
```<img class="img-responsive" src="https://drive.google.com/thumbnail?id=YOUR-IMG-ID-HERE&sz=w1000" data-fancybox alt="A description of your image" width="400" />```
4. Change the _id="_ value to the ID from the "Copy Link" button
5. Change the _alt="_ value to a useful short description of the image
6. Remove the temporary link line from step 3

### Videos
Website videos should all be loaded on the DevilBotz Youtube channel that some members of the team (Dillan, Aadi Dash, Aaliya Hasan, and Bhavya Patel) can contribute to. The channel @burlingtondevilbotz has been created and  can upload to it. Mr. Khan owns the channel and Eleanor is also a manager.

To embed a video, just click the Share button below it and paste that into the blog post inside square brackets:<br /><code>[https://youtu.be/RN6aeRq8kFM]</code>
