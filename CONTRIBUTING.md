## Adding / Modifying a Game in Django Administration

If you are copy-pasting the wiki information from somewhere, please refer the sources by using [NUMBER] in the game description.
Also, make sure to select *Clean Format* button before submitting the text.

### Notes Description

<p>Separate your explanation in paragraphs if needed.</p>
<p><b>Note:</b> Tables are not allowed here at the moment.</p>

### Game Notes

<p>Please insert the explanation here. You can put bullets to clarify your explanation: </p>
<pre>
* This rule is not implemented.
* This feature needs to be polished.
</pre>
<p><b>Note:</b> Tables are not allowed here.</p>

### Game Regulations

#### Description

<p>If you insert a table:</p>

 - Please make sure that the font is `<< System Font >>` and there is no font styling (`font-size: small;` or `font-size:16px`...) in each row when saving it. 
- Please make sure that there is no border styling (`border-color: black;` or `border-size: none;`).
- Please make sure you don't put style on the table in the Admin Text Editor (tinymce); the table style comes with the inline-style of the html file, so don't override it.
- If you have set a table with multiple cells merged (`colspan=X` or `rowspan=X` exists), please make sure there's no `&nbsp;` or `<br />` between the row (or column) and the content. You can examine if the table is properly formatted in *View -> Sources*.

Example of good table formatting:
<pre>
<td style="width: 16.5%; height: 132px; text-align: center;" rowspan="4"><strong>Cartas de la Aluette</strong></td>
</pre>

Example of bad table formatting:
<pre>
<td style="width: 16.5%; height: 132px; text-align: center;" rowspan="4">&nbsp;<br/>&nbsp;<br/><strong>Cartas de la Aluette</strong>&nbsp;<br/>&nbsp;<br/></td>
</pre>

<p><b>Note:</b> In case there is such issue, you can install FoxReplace on Firefox, search each font style and replacing them all by nothing.</p>

<p>What you <b>can do</b> only with the Django Admin Text Editor (tinymce): the first row of the table (the headers, aka column titles) must be bolded.</p>
