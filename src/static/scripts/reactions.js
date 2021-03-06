
function random_element(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

var reaction_emoticons = {
  "good": ["π", "π", "π", "π", "π", "π", "π€©", "π", 
  "π", "π", "π", "π", "π", "π", "π€", "π€", "π", "π€‘", "πͺ", "π", "π", "π­", "π"],
  "bad": ["π₯΅", "π₯΄", "π", "π", "π", "π", "π", "π", 
  "π", "π£", "π", "π©", "πΆ", "π", "π", "π―", "π¦", 
  "π€―", "π³", "π°", "π", "π", "π§", "π€", "π€­", "π¬"],
};

var reaction_texts = {
  "good": ["Super !", "Bravo !", "Tip Top !", "Continue comme Γ§a !", "C'est juste !", 
  "Toi-mΓͺme tu sais !", "VoilΓ  !", "Si si !", "Ouiiii !", "Bien !", "C'est exact !", 
  "Tout juste !", "Excellent !", "TrΓ¨s propre !"],
  "bad": ["Oups !", "Aie...", "Nope...", "Essaie encore", "Encore un effort", "Hmmm, non...", 
  "Tu peux y arriver", "Presque", "Pas tout Γ  fait"],
};

function setup_reactions() {
  var elem = document.createElement("div");
  $(elem).addClass("reactions");
  $("body").append(elem);
}


function create_reaction(type, text, emoticon) {
  if (typeof type != 'string' || (type != 'good' && type != 'bad')) {
    type = "good";
  }

  if (typeof text == 'undefined') {
    text = random_element(reaction_texts[type]);
  }

  if (typeof emoticon == 'undefined') {
    emoticon = random_element(reaction_emoticons[type]);
  }

  var container = document.createElement("div");
  $(container).addClass("reaction");
  $(container).addClass(type);
  var elem = document.createElement("div");
  $(elem).append('<span class="emoticon">' + emoticon + '</span>');
  $(elem).append(text);
  $(container).prepend(elem);
  $(".reactions").prepend(container);
  $(container).animate({opacity: "1"}, 250, "linear");
  setTimeout(hide_reaction(container), 1500);
}

function hide_reaction(container) {
  return function() {
    $(container).animate({marginTop: "200px", opacity: "0"}, 750, "linear", function() {
      $(container).remove();
    });
  };
}

document.addEventListener("DOMContentLoaded", setup_reactions, false);