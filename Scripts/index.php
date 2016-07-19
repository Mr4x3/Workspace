<!DOCTYPE html>
<html>
<head>
   <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
   <title>Directry Lister By Mr.4x3</title>
   <style>
     *{
         padding:0;
         margin:0;
     }
     html,body {
         color:#333;
         font-family: "Lucida Console", Courier, monospace;
         font-size:14px;
         text-shadow:1px 1px 1px #cacaca;
         -webkit-text-shadow:1px 1px 1px #cacaca;
         -moz-text-shadow:1px 1px 1px #cacaca;
     }
     a{
         padding: 2px 0 0 24px;
         color:#FE4902;
         text-decoration:none;
     }
     a:hover{
         color:#000;
     }
     #container{
         margin:0 auto;
         width:700px;
         margin-top:20px;
         padding-top:10px;
         border:1px solid #EEE;
         border-radius:10px;
         -moz-border-radius:10px;
     }
     .head{
         background-color:#FE4902;
         color:#FFF;
         font-weight:bold;
         padding:7px 0 5px 10px;
         font-size:14px;
         letter-spacing:1px;
         font-family: Verdana, Arial, Helvetica, sans-serif;
     }
     .head:hover{background-color:#FE4902;}
     .head span{font-size:9px; letter-spacing:0;}
     td{
         background-color:#F3F3F3;
         padding:6px;
     }
     td:hover{background-color:#EFEFEF;}
     h1{
         font-size:18px;
         font-weight:bold;
         padding:0 0 10px 10px;
     }

     /*icons for file types (add more to suit your needs - icons by famfamfam.)*/

     /*images*/
     a[href$=".jpg"] {background: url(image.gif) no-repeat left 50%;}
     a[href$=".gif"] {background: url(image.gif) no-repeat left 50%;}
     a[href$=".png"] {background: url(image.gif) no-repeat left 0%;}

     /*pdfs*/
     a[href$=".pdf"] {background: url(pdf.gif) no-repeat left 50%;}

     /*psds*/
     a[href$=".psd"] {background: url(psd.gif) no-repeat left 50%;}

     /*docs*/
     a[href$=".doc"] {background: url(doc.gif) no-repeat left 50%;}
     a[href$=".txt"] {background: url(doc.gif) no-repeat left 50%;}

     /*videos*/
     a[href$=".avi"] {background: url(video.gif) no-repeat left 50%;}
     a[href$=".m4a"] {background: url(video.gif) no-repeat left 50%;}
     a[href$=".mov"] {background: url(video.gif) no-repeat left 50%;}
     a[href$=".mp4"] {background: url(video.gif) no-repeat left 50%;}
     a[href$=".wmv"] {background: url(video.gif) no-repeat left 50%;}

     /*audio*/
     a[href$=".mp3"] {background: url(audio.gif) no-repeat left 50%;}
     a[href$=".wma"] {background: url(audio.gif) no-repeat left 50%;}
     a[href$=".aac"] {background: url(audio.gif) no-repeat left 50%;}

     /*web pages*/
     a[href$=".html"] {background: url(html.gif) no-repeat left 50%;}
     a[href$=".php"] {background: url(html.gif) no-repeat left 50%;}

   </style>

</head>
<script type="text/javascript">
//interstitial ad
clicksor_enable_inter = true; clicksor_maxad = -1;
clicksor_hourcap = -1; clicksor_showcap = 2;
//connect widget
clicksor_adhere_opt = 'left:50%';
//default pop-under house ad url
clicksor_enable_pop = true; clicksor_frequencyCap = -1;
durl = 'http://glob.tk';clicksor_enable_layer_pop = false;
//default banner house ad url
clicksor_default_url = 'http://glob.tk';
clicksor_banner_border = ''; clicksor_banner_ad_bg = '';
clicksor_banner_link_color = ''; clicksor_banner_text_color = '';
clicksor_banner_text_banner = false; clicksor_banner_image_banner = true;
clicksor_layer_border_color = '';
clicksor_layer_ad_bg = ''; clicksor_layer_ad_link_color = '';
clicksor_layer_ad_text_color = ''; clicksor_text_link_bg = '';
clicksor_text_link_color = ''; clicksor_enable_text_link = true;
clicksor_layer_banner = false;
</script>




</noscript>

<body>

   <div id="container">
       <?php
         // opens this directory
         $myDirectory = opendir(".");

         // gets each entry
         while($entryName = readdir($myDirectory)) {
           $dirArray[] = $entryName;
         }

         // finds extention of file
         function findexts ($filename)
         {
           $filename = strtolower($filename) ;
           $exts = split("[/\\.]", $filename) ;
           $n = count($exts)-1;
           $exts = $exts[$n];
           return $exts;
         }

         // closes directory
         closedir($myDirectory);

         //  counts elements in array
         $indexCount   = count($dirArray);

         // sorts files
         sort($dirArray);

         // print 'em
         print("<h1>Contents By Blux Xergy</h1>");
         print("<table width='100%' cellspacing='10'>
                 <tr>
                   <td class='head'>Filename</td>
                   <td class='head'>Type</td>
                   <td class='head'>Size <span>(bytes)</span></td></tr>\n");

         // loops through the array of files and print them all
         for($index=0; $index < $indexCount; $index++) {
               if (substr("$dirArray[$index]", 0, 1) != "."){ // don't list hidden files
               print("<tr><td><a href='$dirArray[$index]'>$dirArray[$index]</a></td>");
               print("<td>");
               print(findexts($dirArray[$index]));
               print("</td>");
               print("<td>");
               print(filesize($dirArray[$index]));
               print("</td>");
               print("</tr>\n");
           }
         }
         print("</table>\n");
       ?>
   </div>

</body>

<p class="fc"><a href="http://i4x3.tk/" class="fc">Mr.4x3 | Web</a> - <a href="http://doyl.in/" class="fc">The Doyl Web</a> - <a href="http://u.doyl.in" class="fc">Doyl Web Url Shortner</a> - <a href="http://blog.i4x3.tk" class="fc">Mr.4x3 | Blog</a></p>
<p class="f"><a href="http://i4x3.tk" class="hm">Copyright � 2011 Mr.4x3</a></p>
</html>
