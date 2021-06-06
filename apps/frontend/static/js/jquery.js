$.fn.pageMe = function(opts){

    var $this = this,
        defaults = {
            perPage: 7,
            showPrevNext: false,
            hidePageNumbers: false
        },
        settings = $.extend(defaults, opts);
    
    var listElement = $this.find('tbody');
    var perPage = settings.perPage; 
    var children = listElement.children();
    var pager = $('.pager');
    
    if (typeof settings.childSelector!="undefined") {
        children = listElement.find(settings.childSelector);
    }
    
    if (typeof settings.pagerSelector!="undefined") {
        pager = $(settings.pagerSelector);
    }
    
    var numItems = children.size();
    var numPages = Math.ceil(numItems/perPage);

    pager.data("curr",0);
    
    if (settings.showPrevNext){
        $('<li class="page-item"><a href="#" class="page-link" id="prev_link">«</a></li>').appendTo(pager);
    }
    
    var curr = 0;
    while(numPages > curr && (settings.hidePageNumbers==false)){
        $('<li class="page-item"><a href="#" class="page-link">'+(curr+1)+'</a></li>').appendTo(pager);
        curr++;
    }
    
    if (settings.showPrevNext){
        $('<li class="page-item"><a href="#" class="page-link" id="next_link">»</a></li>').appendTo(pager);
    }
    
    pager.find('.page-link:first').addClass('active');
    pager.find('#prev_link').hide();
    if (numPages<=1) {
        pager.find('#next_link').hide();
    }
    pager.children().eq(1).addClass("active");
    
    children.hide();
    children.slice(0, perPage).show();
    
    pager.find('li .page-link').click(function(){
        var clickedPage = $(this).html().valueOf()-1;
        goTo(clickedPage,perPage);
        return false;
    });
    pager.find('li #prev_link').click(function(){
        previous();
        return false;
    });
    pager.find('li #next_link').click(function(){
        next();
        return false;
    });
    
    function previous(){
        var goToPage = parseInt(pager.data("curr")) - 1;
        goTo(goToPage);
    }
    
    function next(){
        goToPage = parseInt(pager.data("curr")) + 1;
        goTo(goToPage);
    }
    
    function goTo(page){
        var startAt = page * perPage,
            endOn = startAt + perPage;
        
        children.css('display','none').slice(startAt, endOn).show();
        
        if (page>=1) {
            pager.find('#prev_link').show();
        }
        else {
            pager.find('#prev_link').hide();
        }
        
        if (page<(numPages-1)) {
            pager.find('#next_link').show();
        }
        else {
            pager.find('#next_link').hide();
        }
        
        pager.data("curr",page);
        pager.children().removeClass("active");
        pager.children().eq(page+1).addClass("active");
    
    }
};

$(document).ready(function(){
    $('#tabla_espacios').pageMe({pagerSelector:'#paginador1',showPrevNext:true,hidePageNumbers:false,perPage:5});
    $('#tabla_estudiantes').pageMe({pagerSelector:'#paginador2',showPrevNext:true,hidePageNumbers:false,perPage:5});
    $('#tabla_sesiones').pageMe({pagerSelector:'#paginador3',showPrevNext:true,hidePageNumbers:false,perPage:5});
    $('#tabla_tomar_asistencias').pageMe({pagerSelector:'#paginador4',showPrevNext:true,hidePageNumbers:false,perPage:5});
    $('#tabla_tomar_estudiantes').pageMe({pagerSelector:'#paginador5',showPrevNext:true,hidePageNumbers:false,perPage:5});
    $('#tabla_listar_asistencias').pageMe({pagerSelector:'#paginador6',showPrevNext:true,hidePageNumbers:false,perPage:5});
    $('#tabla_listar_estudiantes_asistentes').pageMe({pagerSelector:'#paginador7',showPrevNext:true,hidePageNumbers:false,perPage:5});
});