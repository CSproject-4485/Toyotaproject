Connect-PnPOnline –Url https://myteams.toyota.com/sites/UTD-VendorCostStandardization/ –UseWebLogin

$LibraryName = "Test"  
$Files = Get-PnPFolderItem -FolderSiteRelativeUrl $LibraryName -ItemType File  
foreach($File in $Files) {         
    Get-PnPFile -Url $File.ServerRelativeUrl -Path D:\Downloads -FileName $File.Name -AsFile          
    } 