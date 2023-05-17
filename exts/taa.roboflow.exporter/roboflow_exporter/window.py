__all__ =["RoboflowExportWindow"]#line:1
import omni .ui as ui #line:3
import carb .events #line:4
import omni .kit .app #line:5
from .style import roboflow_export_window_style #line:6
import omni .usd #line:7
from .roboflow_helper import RoboflowHelper #line:9
from .replicator_helper import ReplicatorHelper #line:10
from .upload_helper import UploadHelper #line:11
OOOO0O00O0O0O00O0 =""#line:13
OOO0000O00O0O0OO0 ="C:\\roboflow_export"#line:14
O0OO0OOO000O00O0O ="/World"#line:15
OO0O00OOO0O000000 =10 #line:16
OO0000O0OO00O0OO0 =-100 #line:17
OOOO00000OO0O0OO0 =100 #line:18
O0O00OO00OO0OOO0O =200 #line:19
O00OOOOO0OO00OO00 =300 #line:20
O0OOO0O0O00000OOO =300 #line:21
OOO00OO00O00O00OO =600 #line:22
O0000OO0O000OOO0O =100 #line:24
O0OO0O0O00O0O000O =4 #line:25
class RoboflowExportWindow (ui .Window ):#line:28
    ""#line:29
    def __init__ (O000OOO00OO000O00 ,OOO0OO0OO0OO0O0O0 :str ,delegate =None ,**OOO00O000O0O0OOO0 ):#line:31
        O000OOO00OO000O00 .__O00O0O0O0O0OO0000 =O0000OO0O000OOO0O #line:32
        O000OOO00OO000O00 ._rf =None #line:34
        O000OOO00OO000O00 ._apiKeyField =None #line:35
        O000OOO00OO000O00 ._savePathField =None #line:36
        O000OOO00OO000O00 ._frameCountField =None #line:37
        O000OOO00OO000O00 ._primPathField =None #line:38
        O000OOO00OO000O00 ._xMinField =None #line:39
        O000OOO00OO000O00 ._xMaxField =None #line:40
        O000OOO00OO000O00 ._yMinField =None #line:41
        O000OOO00OO000O00 ._yMaxField =None #line:42
        O000OOO00OO000O00 ._zMinField =None #line:43
        O000OOO00OO000O00 ._zMaxField =None #line:44
        O000OOO00OO000O00 ._projectInfo =None #line:45
        O000OOO00OO000O00 ._projectList =None #line:46
        O000OOO00OO000O00 ._projects =None #line:47
        O000OOO00OO000O00 ._selectedProject =None #line:48
        O000OOO00OO000O00 ._projectObj =None #line:49
        O000OOO00OO000O00 ._setupBtn =None #line:50
        O000OOO00OO000O00 ._startBtn =None #line:51
        O000OOO00OO000O00 ._uploadBtn =None #line:52
        O000OOO00OO000O00 ._uploadStatus =None #line:53
        O000OOO00OO000O00 ._replicatorHelper =ReplicatorHelper ()#line:54
        O000OOO00OO000O00 ._uploadHelper =UploadHelper ()#line:55
        super ().__init__ (OOO0OO0OO0OO0O0O0 ,**OOO00O000O0O0OOO0 )#line:56
        O000OOO00OO000O00 .frame .style =roboflow_export_window_style #line:60
        O000OOO00OO000O00 .frame .set_build_fn (O000OOO00OO000O00 ._build_fn )#line:64
        OO0000000OO0O0OO0 =omni .kit .app .get_app ().get_update_event_stream ()#line:66
        O000OOO00OO000O00 ._sub =OO0000000OO0O0OO0 .create_subscription_to_pop (O000OOO00OO000O00 .on_update ,name ="update subscription")#line:67
    def destroy (OOO00OO0OO00O0OOO ):#line:69
        super ().destroy ()#line:71
        OOO00OO0OO00O0OOO ._sub .unsubscribe ()#line:72
        OOO00OO0OO00O0OOO ._projectList =None #line:73
    def on_update (OOO0O0OO0OO0O0O0O ,OO0O0OOO0OO00OOO0 :carb .events .IEvent ):#line:75
        OOO0O0OO0OO0O0O0O ._uploadHelper .on_update (OO0O0OOO0OO00OOO0 )#line:76
        if OOO0O0OO0OO0O0O0O ._uploadStatus is not None :#line:77
            if OOO0O0OO0OO0O0O0O ._uploadHelper .isReady ():#line:78
                O00OOOOO00O000O00 =OOO0O0OO0OO0O0O0O ._uploadHelper .getRemainingCount ()#line:79
                if O00OOOOO00O000O00 >0 :#line:80
                    OOO0O0OO0OO0O0O0O ._uploadStatus .text ="There are "+str (O00OOOOO00O000O00 )+" files to upload"#line:81
                else :#line:82
                    OOO0O0OO0OO0O0O0O ._uploadStatus .text ="upload complete"#line:83
            else :#line:84
                OOO0O0OO0OO0O0O0O ._uploadStatus .text ="Not initialized"#line:85
    @property #line:87
    def label_width (OO0OOOO0O0O0O000O ):#line:88
        ""#line:89
        return OO0OOOO0O0O0O000O .__O00O0O0O0O0OO0000 #line:90
    @label_width .setter #line:92
    def label_width (OO00OOOO0OOOO0OOO ,OOO000O0O0OO0O0O0 ):#line:93
        ""#line:94
        OO00OOOO0OOOO0OOO .__O00O0O0O0O0OO0000 =OOO000O0O0OO0O0O0 #line:95
        OO00OOOO0OOOO0OOO .frame .rebuild ()#line:96
    def connect_to_roboflow (O0000O00O0O0OOOOO ):#line:98
        if O0000O00O0O0OOOOO ._rf is None :#line:99
            O00OO00OO0O000OO0 =O0000O00O0O0OOOOO ._apiKeyField .model .get_value_as_string ()#line:100
            print (O00OO00OO0O000OO0 )#line:101
            try :#line:102
                O0000O00O0O0OOOOO ._rf =RoboflowHelper (api_key =O00OO00OO0O000OO0 )#line:103
                OO0O00O0O00O00O00 =O0000O00O0O0OOOOO ._rf .workspace ()#line:104
                print (OO0O00O0O00O00O00 )#line:105
                O0000O00O0O0OOOOO ._projectInfo .text =OO0O00O0O00O00O00 .name #line:106
                O0000O00O0O0OOOOO ._projects =OO0O00O0O00O00O00 .projects ()#line:107
                for O0O000OO0OO000O0O in O0000O00O0O0OOOOO ._projects :#line:109
                    O0000O00O0O0OOOOO ._projectList .model .append_child_item (None ,ui .SimpleStringModel (O0O000OO0OO000O0O ))#line:110
                O0000O00O0O0OOOOO ._projectList .visible =True #line:112
                O0000O00O0O0OOOOO ._connectButton .visible =False #line:113
                O0000O00O0O0OOOOO ._setupBtn .visible =True #line:115
            except Exception :#line:116
                O0000O00O0O0OOOOO ._projectInfo .text ="Invalid Key"#line:117
        else :#line:118
            O0000O00O0O0OOOOO ._rf =None #line:119
            O0000O00O0O0OOOOO ._connectButton .text ="Connect"#line:120
            O0000O00O0O0OOOOO ._projectInfo .text =""#line:121
    def project_changed (O00OOOOO00O0O0000 ,OO00000OO0000OO0O ,O00O00O0O00OO0OOO ):#line:123
        try :#line:124
            OO0O000O0O00OOO0O =OO00000OO0000OO0O .get_item_value_model ().as_int #line:125
            O00OOOOO00O0O0000 ._selectedProject =O00OOOOO00O0O0000 ._projects [OO0O000O0O00OOO0O -1 ]#line:126
            O00OOOOO00O0O0000 ._projectObj =O00OOOOO00O0O0000 ._rf .project (O00OOOOO00O0O0000 ._selectedProject )#line:127
            print (O00OOOOO00O0O0000 ._selectedProject )#line:128
        except Exception :#line:129
            print ("error")#line:130
    def setup_replicator (O00OO0O000OO000O0 ):#line:132
        if O00OO0O000OO000O0 ._projectObj is not None :#line:133
            O0000O0000O0O000O =O00OO0O000OO000O0 ._savePathField .model .get_value_as_string ()#line:134
            OOOOOO00O0O00O0OO =O00OO0O000OO000O0 ._xMinField .model .get_value_as_float ()#line:135
            O00OOO000000O0OO0 =O00OO0O000OO000O0 ._xMaxField .model .get_value_as_float ()#line:136
            OO0000O0O00O000OO =O00OO0O000OO000O0 ._yMinField .model .get_value_as_float ()#line:137
            OO0O0O0OOOOO0OOOO =O00OO0O000OO000O0 ._yMaxField .model .get_value_as_float ()#line:138
            O000OO000O0OO000O =O00OO0O000OO000O0 ._zMinField .model .get_value_as_float ()#line:139
            OO0OO0O0O00OOO00O =O00OO0O000OO000O0 ._zMaxField .model .get_value_as_float ()#line:140
            OO0O0OOO0O0O00O00 =O00OO0O000OO000O0 ._frameCountField .model .get_value_as_int ()#line:141
            O00O00OOO000OO0OO =O00OO0O000OO000O0 ._primPathField .model .get_value_as_string ()#line:142
            O00OO0O000OO000O0 ._replicatorHelper .setup (O0000O0000O0O000O ,OOOOOO00O0O00O0OO ,O00OOO000000O0OO0 ,OO0000O0O00O000OO ,OO0O0O0OOOOO0OOOO ,O000OO000O0OO000O ,OO0OO0O0O00OOO00O ,OO0O0OOO0O0O00O00 ,O00O00OOO000OO0OO )#line:143
            O00OO0O000OO000O0 ._setupBtn .visible =False #line:144
            O00OO0O000OO000O0 ._startBtn .visible =True #line:145
            O0000O0000O0O000O =O00OO0O000OO000O0 ._savePathField .model .get_value_as_string ()#line:147
            O00OO0O000OO000O0 ._uploadHelper .setup (O0000O0000O0O000O ,O00OO0O000OO000O0 ._projectObj )#line:148
            O00OO0O000OO000O0 ._replicatorStatus .text ="Setup complete, ready to start"#line:149
    def start_replicator (OO0O000O000O00OO0 ):#line:151
        OO0O000O000O00OO0 ._replicatorHelper .start ()#line:154
        OO0O000O000O00OO0 ._startBtn .visible =False #line:155
        OO0O000O000O00OO0 ._replicatorStatus .text =""#line:156
    def select_prims (OO0OO000O0OO0000O ):#line:158
        O0OO0O0OO0O00OOOO =omni .usd .get_context ()#line:159
        OO00000O0O0OOOO00 =O0OO0O0OO0O00OOOO .get_selection ().get_selected_prim_paths ()#line:160
        print (OO00000O0O0OOOO00 )#line:161
        OO0OOOO0O00O00O00 =",".join (OO00000O0O0OOOO00 )#line:162
        OO0OO000O0OO0000O ._primPathField .model .set_value (OO0OOOO0O00O00O00 )#line:163
    def _build_collapsable_header (O000000000000000O ,OO0OOOOOO00O0000O ,OO0O000O00000OOO0 ):#line:165
        ""#line:166
        with ui .HStack ():#line:167
            ui .Label (OO0O000O00000OOO0 ,name ="collapsable_name")#line:168
            if OO0OOOOOO00O0000O :#line:170
                OOOOO0O000O00OO00 ="collapsable_opened"#line:171
            else :#line:172
                OOOOO0O000O00OO00 ="collapsable_closed"#line:173
            ui .Image (name =OOOOO0O000O00OO00 ,width =20 ,height =20 )#line:174
    def _build_roboflow (OO000O0O0O0OOO0OO ):#line:176
        ""#line:177
        with ui .CollapsableFrame ("1 - Roboflow",name ="group",build_header_fn =OO000O0O0O0OOO0OO ._build_collapsable_header ):#line:178
            with ui .VStack (height =0 ,spacing =O0OO0O0O00O0O000O ):#line:179
                with ui .HStack ():#line:180
                    ui .Label ("API Key",name ="attribute_name",width =O0000OO0O000OOO0O )#line:181
                    OO000O0O0O0OOO0OO ._apiKeyField =ui .StringField ()#line:182
                OO000O0O0O0OOO0OO ._apiKeyField .model .set_value (OOOO0O00O0O0O00O0 )#line:183
                OO000O0O0O0OOO0OO ._connectButton =ui .Button ("Connect",clicked_fn =OO000O0O0O0OOO0OO .connect_to_roboflow )#line:184
                OO000O0O0O0OOO0OO ._projectInfo =ui .Label ("Not connected")#line:185
                OO000O0O0O0OOO0OO ._projectList =ui .ComboBox (0 ,"Select a project",name ="Projects",height =10 ,visible =False )#line:192
                OO000O0O0O0OOO0OO ._projectList .model .add_item_changed_fn (OO000O0O0O0OOO0OO .project_changed )#line:194
    def _build_output (OOO0000OO000OO00O ):#line:196
        with ui .CollapsableFrame ("2 - Output",name ="group",build_header_fn =OOO0000OO000OO00O ._build_collapsable_header ):#line:197
            with ui .VStack (height =0 ,spacing =O0OO0O0O00O0O000O ):#line:198
                with ui .HStack ():#line:199
                    ui .Label ("Save To Path",name ="attribute_name",width =O0000OO0O000OOO0O )#line:200
                    OOO0000OO000OO00O ._savePathField =ui .StringField ()#line:201
                    OOO0000OO000OO00O ._savePathField .model .set_value (OOO0000O00O0O0OO0 )#line:202
    def _build_selection (OOO0OOOOO0000O0OO ):#line:204
        with ui .CollapsableFrame ("3 - Selection",name ="group",build_header_fn =OOO0OOOOO0000O0OO ._build_collapsable_header ):#line:205
            with ui .VStack (height =0 ,spacing =O0OO0O0O00O0O000O ):#line:206
                with ui .HStack ():#line:207
                    ui .Label ("Prim path(s)",name ="attribute_name",width =O0000OO0O000OOO0O )#line:208
                    OOO0OOOOO0000O0OO ._primPathField =ui .StringField ()#line:209
                    OOO0OOOOO0000O0OO ._primPathField .model .set_value (O0OO0OOO000O00O0O )#line:210
                OOO0OOOOO0000O0OO ._selectButton =ui .Button ("Grab Selection",clicked_fn =OOO0OOOOO0000O0OO .select_prims )#line:211
    def _build_framecount (O0OO0O0000O00O0OO ):#line:214
        with ui .CollapsableFrame ("4 - Number of Frames",name ="group",build_header_fn =O0OO0O0000O00O0OO ._build_collapsable_header ):#line:215
            with ui .VStack (height =0 ,spacing =O0OO0O0O00O0O000O ):#line:216
                with ui .HStack ():#line:217
                    ui .Label ("Frames",name ="attribute_name",width =O0000OO0O000OOO0O )#line:218
                    O0OO0O0000O00O0OO ._frameCountField =ui .StringField ()#line:219
                    O0OO0O0000O00O0OO ._frameCountField .model .set_value (OO0O00OOO0O000000 )#line:220
    def _build_camera (OO0O0OOOOOOO0O0O0 ):#line:222
        with ui .CollapsableFrame ("5 - Camera",name ="group",build_header_fn =OO0O0OOOOOOO0O0O0 ._build_collapsable_header ):#line:223
            with ui .VStack (height =0 ,spacing =O0OO0O0O00O0O000O ):#line:224
                with ui .HStack ():#line:225
                    ui .Label ("X Min",name ="attribute_name",width =OO0O0OOOOOOO0O0O0 .label_width )#line:226
                    OO0O0OOOOOOO0O0O0 ._xMinField =ui .FloatSlider (name ="attribute_float",min =-1000 ,max =1000 )#line:227
                    OO0O0OOOOOOO0O0O0 ._xMinField .model .set_value (OO0000O0OO00O0OO0 )#line:228
                with ui .HStack ():#line:230
                    ui .Label ("X Max",name ="attribute_name",width =OO0O0OOOOOOO0O0O0 .label_width )#line:231
                    OO0O0OOOOOOO0O0O0 ._xMaxField =ui .FloatSlider (name ="attribute_float",min =-1000 ,max =1000 )#line:232
                    OO0O0OOOOOOO0O0O0 ._xMaxField .model .set_value (OOOO00000OO0O0OO0 )#line:233
                with ui .HStack ():#line:235
                    ui .Label ("Y Min",name ="attribute_name",width =OO0O0OOOOOOO0O0O0 .label_width )#line:236
                    OO0O0OOOOOOO0O0O0 ._yMinField =ui .FloatSlider (name ="attribute_float",min =-1000 ,max =1000 )#line:237
                    OO0O0OOOOOOO0O0O0 ._yMinField .model .set_value (O0O00OO00OO0OOO0O )#line:238
                with ui .HStack ():#line:240
                    ui .Label ("Y Max",name ="attribute_name",width =OO0O0OOOOOOO0O0O0 .label_width )#line:241
                    OO0O0OOOOOOO0O0O0 ._yMaxField =ui .FloatSlider (name ="attribute_float",min =-1000 ,max =1000 )#line:242
                    OO0O0OOOOOOO0O0O0 ._yMaxField .model .set_value (O00OOOOO0OO00OO00 )#line:243
                with ui .HStack ():#line:245
                    ui .Label ("Z Min",name ="attribute_name",width =OO0O0OOOOOOO0O0O0 .label_width )#line:246
                    OO0O0OOOOOOO0O0O0 ._zMinField =ui .FloatSlider (name ="attribute_float",min =-1000 ,max =1000 )#line:247
                    OO0O0OOOOOOO0O0O0 ._zMinField .model .set_value (O0OOO0O0O00000OOO )#line:248
                with ui .HStack ():#line:250
                    ui .Label ("Z Max",name ="attribute_name",width =OO0O0OOOOOOO0O0O0 .label_width )#line:251
                    OO0O0OOOOOOO0O0O0 ._zMaxField =ui .FloatSlider (name ="attribute_float",min =-1000 ,max =1000 )#line:252
                    OO0O0OOOOOOO0O0O0 ._zMaxField .model .set_value (OOO00OO00O00O00OO )#line:253
    def _build_replicator (OOO0OO00000O0OOO0 ):#line:255
        with ui .CollapsableFrame ("6 - Replicator",name ="group",build_header_fn =OOO0OO00000O0OOO0 ._build_collapsable_header ):#line:256
            with ui .VStack (height =0 ,spacing =O0OO0O0O00O0O000O ):#line:257
                with ui .HStack ():#line:258
                    OOO0OO00000O0OOO0 ._setupBtn =ui .Button ("Setup",clicked_fn =OOO0OO00000O0OOO0 .setup_replicator )#line:259
                    OOO0OO00000O0OOO0 ._setupBtn .visible =False #line:260
                with ui .HStack ():#line:261
                    OOO0OO00000O0OOO0 ._startBtn =ui .Button ("Start",clicked_fn =OOO0OO00000O0OOO0 .start_replicator )#line:262
                    OOO0OO00000O0OOO0 ._startBtn .visible =False #line:263
                with ui .HStack ():#line:264
                    OOO0OO00000O0OOO0 ._replicatorStatus =ui .Label ("Setup required",name ="upload_status",width =O0000OO0O000OOO0O )#line:265
    def _build_uploader (O000O000OOO0O00OO ):#line:267
         with ui .CollapsableFrame ("7 - Upload Status",name ="group",build_header_fn =O000O000OOO0O00OO ._build_collapsable_header ):#line:268
            with ui .VStack (height =0 ,spacing =O0OO0O0O00O0O000O ):#line:269
                with ui .HStack ():#line:270
                    O000O000OOO0O00OO ._uploadStatus =ui .Label ("Nothing to upload",name ="upload_status",width =O0000OO0O000OOO0O )#line:271
    def _build_fn (O0000OOO0O000O0OO ):#line:273
        ""#line:277
        with ui .ScrollingFrame ():#line:278
            with ui .VStack (height =0 ):#line:279
                O0000OOO0O000O0OO ._build_roboflow ()#line:280
                O0000OOO0O000O0OO ._build_output ()#line:281
                O0000OOO0O000O0OO ._build_selection ()#line:282
                O0000OOO0O000O0OO ._build_framecount ()#line:283
                O0000OOO0O000O0OO ._build_camera ()#line:284
                O0000OOO0O000O0OO ._build_replicator ()#line:285
                O0000OOO0O000O0OO ._build_uploader ()#line:286
