//关卡页面20波强度最大为10
oS.Init({
		PName:[oPeashooter,oCherryBomb,oWallNut,oLilyPad],
		ZName:[oSmallZombie,oSmallDuckyTubeZombie1,oSmallConeheadZombie,oSmallFootballZombie,oSmallSnorkelZombie], //本关所有的僵尸类名
		//储存本关除了僵尸和植物以外的其他图片地址，比如背景、奖杯等，常用的其他图片比如阳光、界面等都在0关缓存了
		PicArr:function(){
			var Pro=oJalapeno.prototype,PicArr=Pro.PicArr;
			return ['images/interface/background3.jpg',
				PicArr[Pro.CardGif],PicArr[Pro.NormalGif]]
		}(),
		Coord:2, //水池坐标系
		SunNum:50,
		LF:[0,1,1,2,2,1,1], //水池地形
		backgroundImage:'images/interface/background3.jpg', //本关的背景图片
		CanSelectCard:0, //是否可以选卡
		StaticCard:0, //非固定卡片
		LevelName:'关卡 3-5', //关卡名
		LvlEName:25,
		FlagZombie:oSmallFlagZombie, //旗帜僵尸用小僵尸
		LargeWaveFlag:{10:$('imgFlag3'),20:$('imgFlag1')}, //第几波使用哪个旗子
		UserDefinedFlagFunc:function($T){ //最后一波时从水里6-9列出来3僵尸
			oP.FlagNum==oP.FlagZombies&&oP.SetTimeoutWaterZombie(6,9,3,[oDuckyTubeZombie1])
		},
		StartGameMusic:'Kitanai Sekai.swf',
		LoadAccess:function(CallBack){
			EDAll.scrollLeft=0;
			NewImg('dDave','images/interface/Dave.gif','left:0;top:81px;z-index:20',EDAll);
			NewEle('DivTeach','div',0,0,EDAll);
			(function(LevelTeachStep){
					//教学
					var callee=arguments.callee,DivTeach=$('DivTeach');
					switch(LevelTeachStep){
						case 0:
							DivTeach.innerHTML='<span style="font-size:22px">僵尸的进攻计划其实是件很有趣的事情。有时候他们会来的很少。(点击继续)</span>';
							DivTeach.onclick=function(){oSym.addTask(10,callee,[1])};
							break;
						case 1:
							innerText(DivTeach,'很少但很划算！(点击继续)');
							DivTeach.onclick=function(){oSym.addTask(10,callee,[2])};
							break;
						case 2:
							innerText(DivTeach,'防守好你的小腿吧！(点击继续)');
							DivTeach.onclick=function(){oSym.addTask(10,callee,[3])};
							break;
						case 3:
							DivTeach.onclick=null;
							ClearChild(DivTeach);
							$('dDave').src='images/interface/Dave2.gif';
							oSym.addTask(50,function(){
								ClearChild($('dDave'));
								var _this=oS;
								NewImg('imgGrowSoil','images/interface/GrowSoil.png','visibility:hidden;z-index:50',EDPlants); //种植土壤图片
								NewEle('dTitle','div',0,0,EDAll); //卡片提示div
								innerText(ESSunNum,_this.SunNum);
								InitPCard();
								oS.ScrollScreen();
							},[]);
					}
				})(0); //全局监控计时器
		},
		StartGame:function(){
			//开始
			!oS.Silence&&NewMusic('UraniwaNi.swf');
			SetVisible($('tdShovel'),$('dFlagMeter'),$('dTop')); //有铲子
			SetHidden($('dSunNum')); //不显示阳光
			oS.InitLawnMower(); //剪草机
			PrepareGrowPlants(function(){ //开局直接刷僵尸
				oP.Monitor({f:function(){
					(function(){ //6秒给一次卡片的计时器
						var L=ArCard.length;
						if(L<10){
							var Ar=oS.PName,P,Pro,id='dCard'+Math.random(),i=Math.floor(Math.random()*100); //取0-99随机数
							switch(true){
								case i<40:P=oCherryBomb;break;
								case i<70:P=oPeashooter;break;
								case i<90:P=oWallNut;break;
								default:P=oLilyPad;
							}
							Pro=P.prototype;
							ArCard[L]={DID:id,PName:P,PixelTop:600};
							NewImg(id,Pro.PicArr[Pro.CardGif],'top:600px;cursor:pointer',$('dCardList'),{onmouseover:function(event){ViewPlantTitle(GetChoseCard(id),event)},onmouseout:function(){SetHidden($('dTitle'))},onclick:function(event){ChosePlant(event,oS.ChoseCard,id)}});
						};
						oSym.addTask(600,arguments.callee,[]);
					})();
					(function(){ //移动卡片的计时器
						var i=ArCard.length,Ar,offsetTop;
						while(i--)(offsetTop=(Ar=ArCard[i]).PixelTop)>60*i&&($(Ar.DID).style.top=(Ar.PixelTop=offsetTop-1)+'px');
						oSym.addTask(5,arguments.callee,[]);
					})();	
				},ar:[]}); //全局监控计时器
				oP.AddZombiesFlag();
				SetVisible($('dFlagMeterContent'));
			});
		}
	},{
		AZ:[[oSmallZombie,7,1],[oSmallDuckyTubeZombie1,1,6,[6,7,8,10,20,29,30]],[oSmallConeheadZombie,4,1],[oSmallFootballZombie,1,1],[oSmallSnorkelZombie,1,7,[29,30]]],
		FlagNum:20, //僵尸波数
		FlagToSumNum:{a1:[3,5,9,10,13,15,19],a2:[3,10,20,40,30,40,50,60]}, //代表第1-3波强度是1，4-5是2，6-9是3，其余是10
		FlagToMonitor:{9:[ShowLargeWave,0],19:[ShowFinalWave,0]},
		FlagToEnd:function(){
			NewImg('imgSF','images/Card/Plants/Jalapeno.png','left:627px;top:325px',EDAll,{onclick:function(){GetNewCard(this,oJalapeno,26)}});
			NewImg('PointerUD','images/interface/PointerDown.gif','top:290px;left:636px',EDAll); //上下箭头图片
		}
	},{ //以下为改写原全局函数，在重新选关后会重置会原函数
		//选择植物
		GetChoseCard:function(id){
			var i=ArCard.length;
			while(i--)ArCard[i].DID==id&&(oS.ChoseCard=i,i=0);
			return oS.ChoseCard;
		},
		ChosePlant:function(evt,i){
			evt=window.event||evt;
			var AC=ArCard[oS.ChoseCard],evtX=evt.clientX-EDAlloffsetLeft+EBody.scrollLeft||EElement.scrollLeft,evtY=evt.clientY+EBody.scrollTop||EElement.scrollTop,Pro=AC.PName.prototype;
			oS.Chose=1;
			EditImg((EditImg($Pn[Pro.EName].childNodes[1].cloneNode(false),'MovePlant','',{left:evtX-.5*(Pro.beAttackedPointL+Pro.beAttackedPointR)+'px',top:evtY+20-Pro.height+'px',zIndex:254},EDAll)).cloneNode(false),'MovePlantAlpha','',{visibility:'hidden',filter:'alpha(opacity=40)',opacity:.4,zIndex:30},EDAll);
			SetAlpha($(AC.DID),50,.5);
			SetHidden($('dTitle'));
			GroundOnmousemove=GroundOnmousemove1;
		},
		//放弃种植 参数不需要传递
		CancelPlant:function(){
			ClearChild($('MovePlant'),$('MovePlantAlpha'));
			oS.Chose=0;
			SetAlpha($(ArCard[oS.ChoseCard].DID),100,1);
			oS.ChoseCard='';
			GroundOnmousemove=function(){};
		},
		//种植植物
		GrowPlant:function(AP,X,Y,R,C){
			var ChoseCard=oS.ChoseCard,AC=ArCard[ChoseCard],P=AC.PName,Pro=P.prototype,CID=AC.DID,card;
			Pro.CanGrow(AP,R,C)&&
			function(){
				(new P).Birth(X,Y,R,C,AP);
				oSym.addTask(20,SetNone,[SetStyle($('imgGrowSoil'),{left:X-30+'px',top:Y-40+'px',zIndex:3*R,visibility:'visible'})]); //消失土壤
				ClearChild($('MovePlant'),$('MovePlantAlpha'));
				$('dCardList').removeChild(card=$(CID));
				card=null;
				ArCard.splice(ChoseCard,1);
				oS.ChoseCard='';
				oS.Chose=0;
				GroundOnmousemove=function(){};
			}();
		},
		ViewPlantTitle:function(i){ //模拟img.title
			var d=$('dTitle'),Pro=ArCard[i].PName.prototype;
			d.innerHTML=Pro.CName+'<br>'+Pro.Tooltip;
			SetStyle(d,{top:60*i+'px',left:'100px'});
		}
});