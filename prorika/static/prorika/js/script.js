const elem=document.getElementsByClassName('user');

const header_links=document.getElementsByClassName('act');

const search_field=document.querySelector('#searchField');
const table_output=document.querySelector('.table-output');
const tbody=document.querySelector('.tbody');
const not_found=document.querySelector('#not_found');
const search_output=document.querySelector('.search-output')
search_output.style.display='none'

search_field.addEventListener('keyup',(e)=>{
   value=e.target.value;
   if(value.length>0){
  fetch('/searchproblems',{
   method:"POST",
   body:JSON.stringify({'search_text':value})
  }
  ).then(data=>data.json()).then(result=>{
   table_output.classList.add('hidden');
   search_output.style.display='block'
   tbody.innerHTML=''; 
   not_found.innerHTML='';
   if(result.length==0){
     search_output.style.display='none';
      not_found.innerHTML='NO DATA FOUND';
   }
   else{
      result.forEach(problem=>{
         console.log(problem)
         tbody.innerHTML+=`
         <tr>
         <td>${ problem.name}</td>
         <td>${problem.description}</td>
         <td>
            
          ${problem.is_completed}

         </td>
         <td>
            ${problem.website}
         </td>
         <td>
         
            <a href="/problem/${problem.id}">
               <i class="fa fa-eye btn btn-primary"></i>
            </a>
            <a href="/problem-update/${problem.id}">
               <i class="fa fa-pencil btn btn-primary"></i>
            </a>

         </td>
         </tr>

         `
      })  
   }

  })
}
else{
   not_found.innerHTML=''
   search_output.style.display='none';
   table_output.classList.remove('hidden');
}
});




Array.from(header_links).forEach(element => {
   console.log(element);
   element.addEventListener('click',(e)=>{
      em=e.target;
      em.classList.toggle('active');
   });
});


for(var i=0;i<elem.length;i++){
   elem[i].addEventListener('hover',function(){
      elem[i].classList.toggle('active');
      elem[i].classList.toggle('user');

   });
   
}





