/*
 * Javascript Timer
 * https://github.com/TheBestCoders/Javascript-Timer
 * Copyright (c) 2015 -	TheBestCoders (Alauddin Ansari)
 * Licensed under the GNU license (http://opensource.org/licenses/GPL-3.0)
 * Version: 0.0.1
 * Dependencies: This javascript plugin uses 'Cookies'.
 * Uses:
 * // include timer.js file and then
 * timer.init(); // Initiate timer instance
 * document.addEventListener('updateTimer', function(e){
 *     document.getElementById('mytimer').innerHTML = e.detail.time;
 * });
 */

if (!Date.now) {
	Date.now = function() { return new Date().getTime(); }
}

var timer = {
	evt: {},
	counts: 0,
	seconds: 0,
	minutes: 0,
	hours: 0,
	timestamp: 0,
	pausestamp: 0,
	life: 30, // how long timer should be keep running (in days)
	time: "",
	isRunning: false,
	init: function()
	{
		var ct = Date.now();
		this.isRunning = (this.getCookie('isTimerRunning') === 'true');
		this.timestamp = this.getCookie('aTimer');
		this.pausestamp = this.getCookie('pTimer');

		if(this.pausestamp == "") this.pausestamp = 0;

		if(this.pausestamp > 0)
			this.timestamp = (ct - (this.pausestamp - this.timestamp));

		if(this.timestamp == "" || this.timestamp == 0)
			this.counts = 0;
		else
			this.counts = Math.floor((ct - this.timestamp) / 1000);

		if(this.isRunning){
			this.start(true);
		}
		else
			this.update();
	},
	start: function(initiate)
	{
		if(!this.isRunning || initiate)
		{
			if(!initiate)
				this.timestamp = ((Date.now()/1000) - this.counts) * 1000;
			this.isRunning = true;
			this.setCookie('aTimer', this.timestamp);
			this.setCookie('pTimer', 0);
			this.setCookie('isTimerRunning', 'true');
			this.update();
		}
	},
	pause: function()
	{
		if(this.isRunning)
		{
			this.isRunning = false;
			this.setCookie('isTimerRunning', 'false');
			this.setCookie('pTimer', Date.now());
		}
	},
	setStartTime: function(seconds)
	{
		this.counts = seconds;
		this.timestamp = ((Date.now()/1000) - this.counts) * 1000;
		this.setCookie('aTimer', this.timestamp);
		if(!this.isRunning){
			this.setCookie('pTimer', Date.now());
			this.update();
		}
	},
	reset: function()
	{
		this.counts = 0;
		this.pausestamp = 0;
		this.timestamp = (this.isRunning ? Date.now() : 0);
		this.setCookie('aTimer', this.timestamp);
		this.setCookie('pTimer', this.pausestamp);

		this.time = "00:00:00";
		this.evt = new CustomEvent('updateTimer', {'detail':{
			'time': this.time,
			'hours': 0,
			'minutes': 0,
			'seconds': 0,
		}});
		document.dispatchEvent(this.evt);
	},
	update: function()
	{
		this.hours = Math.floor(this.counts / 60 / 60);
		this.minutes = Math.floor(this.counts / 60) - (this.hours * 60);
		this.seconds = this.counts - (this.minutes * 60) - (this.hours * 60 * 60);

		this.hours = (this.hours < 10) ? '0'+this.hours : this.hours;
		this.minutes = (this.minutes < 10) ? '0'+this.minutes : this.minutes;
		this.seconds = (this.seconds < 10) ? '0'+this.seconds : this.seconds;

		this.time = this.hours+':'+this.minutes+':'+this.seconds;
		this.evt = new CustomEvent('updateTimer', {'detail':{
			'time': this.time,
			'hours': this.hours,
			'minutes': this.minutes,
			'seconds': this.seconds,
		}});
		document.dispatchEvent(this.evt);

		this.counts++;
		setTimeout(function(){
			if(timer.isRunning)
				timer.update();
		}, 1000);
	},
	setCookie: function(cname, cvalue)
	{
		var d = new Date();
		d.setTime(d.getTime() + (this.life*24*60*60*1000));
		var expires = "expires="+d.toUTCString();
		document.cookie = cname + "=" + cvalue + "; " + expires;
	},
	getCookie: function(cname)
	{
		var name = cname + "=";
		var ca = document.cookie.split(';');
		for(var i=0; i<ca.length; i++) {
			var c = ca[i];
			while (c.charAt(0)==' ')
				c = c.substring(1);
			if (c.indexOf(name) == 0)
				return c.substring(name.length,c.length);
		}
		return "";
	},
};