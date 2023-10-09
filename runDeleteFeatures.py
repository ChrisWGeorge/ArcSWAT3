import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "c:/data"

in_features = arcpy.GetParameterAsText(0)

arcpy.DeleteFeatures_management(in_features)

# The following message will be included in the message box from the calling button's OnClick routine
print("Deletion of selected features from {0} complete.", in_features)

