-	How big is the dataset?
    with ls -lh file_name.csv we get human readable informations. 
    -rw-rw-r-- 1 antoninberanger antoninberanger 4.7M Oct 19  2019 clean_dialog.csv
    clean_dialog.csv is 4.7M. 

-	What’s the structure of the data? (i.e., what are the field and what are values in them)
    with head -n 1 clean_dialog.csv we can get the fields (name of columns) : 
        => "title","writer","pony","dialog"
    with head -n 2 clean_dialog.csv we can see the 2 first lines :
        => there are only Strings in this csv file. 

-	How many episodes does it cover?
    Using cut -d ',' -f1 clean_dialog.csv | tail -n +2 | uniq | wc -l, we can tell that clean_dialog.csv treats 196 episodes. 
    cut -d ',' -f1 clean_dialog.csv: this extracts the "title" column.
    tail -n +2: this skips line 1 (column name) and goes through the all file.
    uniq: this keeps uniq episode title. 
    wc -l: this counts the number of lines remaining. 

-	During the exploration phase, find at least one aspect of the dataset that is unexpected – meaning that it seems like it could create issues for later analysis.
    Each row represents a line of dialogue, but the text can include commas or quotes, which might be misinterpreted as column separators if the CSV isn’t properly quoted. Also, multi-sentence dialogues can also include line breaks, which could make some CSV parsers treat one row as multiple rows. Finally, non-standard characters (like fancy quotes, accented letters, or emojis) could cause encoding issues if the file is not read in UTF-8.
