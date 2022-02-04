#ifndef CORPORATEBORROWER_H
#define CORPORATEBORROWER_H
#include "Borrower.h"

#include <string>

/**
  * class CorporateBorrower
  * 
  */

class CorporateBorrower : public Borrower
{
public:

  // Constructors/Destructors
  //  


  /**
   * Empty Constructor
   */
  CorporateBorrower ();

  /**
   * Empty Destructor
   */
  ~CorporateBorrower ();

  // Static Public attributes
  //  

  // Public attributes
  //  


  // Public attribute accessor methods
  //  


  // Public attribute accessor methods
  //  


protected:

  // Static Protected attributes
  //  

  // Protected attributes
  //  

public:


  // Protected attribute accessor methods
  //  

protected:

public:


  // Protected attribute accessor methods
  //  

protected:


private:

  // Static Private attributes
  //  

  // Private attributes
  //  

  // The market capitalization of a company
  float market_capitalization;
public:


  // Private attribute accessor methods
  //  

private:

public:


  // Private attribute accessor methods
  //  


  /**
   * Set the value of market_capitalization
   * The market capitalization of a company
   * @param new_var the new value of market_capitalization
   */
  void setMarket_capitalization (float new_var)   {
      market_capitalization = new_var;
  }

  /**
   * Get the value of market_capitalization
   * The market capitalization of a company
   * @return the value of market_capitalization
   */
  float getMarket_capitalization ()   {
    return market_capitalization;
  }
private:


  void initAttributes () ;

};

#endif // CORPORATEBORROWER_H
