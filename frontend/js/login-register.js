function Validator(option)
{
  function validated(rule,inputElement)
  {
     var errorMessage 
     var errorElement = inputElement.parentElement.querySelector('.form-message')
     var rules = selectorRules[rule.selector]
     for(var i = 0; i < rules.length; i++ )
     {
      errorMessage = rules[i](inputElement.value)
      break
     }
  
      if(errorMessage)
      {
        errorElement.innerText = errorMessage
        inputElement.parentElement.classList.add('invalid')    
      }
      else
      {
        errorElement.innerText = ""
        inputElement.parentElement.classList.remove('invalid')
      }
      return !errorMessage
      
  }

  var selectorRules ={}

  var formElement = document.querySelector(option.form)
  
  if(formElement)
  {
    formElement.onsubmit = function(e)
    {
      e.preventDefault()
      var isFormValid = true

      option.rules.forEach(function(rule){
        var inputElement = formElement.querySelector(rule.selector) 
        var isValid = validated(rule,inputElement)
        if(!isValid) isFormValid = false
      })    
      
      if(isFormValid){
        formElement.submit();       
      }   
    }
    
    option.rules.forEach(function(rule)
  {
    // luu lai cac rule trong moi input
    if(Array.isArray(selectorRules[rule.selector])){
      selectorRules[rule.selector].push(rule.test)
    }
    else{
      selectorRules[rule.selector] = [rule.test]
    }
    
  
    var inputElement = formElement.querySelector(rule.selector)

    if(inputElement)
    {
      inputElement.onblur = function()
    {
      validated(rule,inputElement)  
    } 
      inputElement.oninput  = function()
      {
        var errorElement = inputElement.parentElement.querySelector('.form-message')
        errorElement.innerText = ""
        inputElement.parentElement.classList.remove('invalid')
      }
    }  
  })
  }
}

Validator.isRequired = function(selector)
{
  return {
    selector: selector,
    test: function(value)
    {
      return value ? undefined : "Vui long nhap gia tri"
    }
  }
}

Validator.isEmail = function(selector)
{
  return {
    selector: selector,
    test: function(value)
    {
      var regex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
      return regex.test(value) ? undefined : "Nhap email cua ban"
    }
  }
}

Validator.minLength = function(selector,min)
{
  return {
    selector: selector,
    test: function(value)
    {
      return value.length >= min ? undefined : "Nhap it nhat 6 ki tu"
    }
  }
}

Validator.confirmPassword = function(selector,password)
{
  return {
    selector: selector,
    test: function(value)
    {
      return value == password() ? undefined : "Nhap lai chinh xac mat khau"
    }
  }
}


var address = 'https://jsonplaceholder.typicode.com/todos/1'
fetch(address)
    .then(function(response){
      return response.json()      
    })
    .then(function(data){
      console.log(data)
    })
    .catch(function(){
      console.log('error')
    })
    .finally(function(){
      console.log('success')
    })





