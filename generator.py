import data.oracle as oracle
import data.mongo as mongo
import data.reference as reference


def generateOrderPool(nbOrders=0):
    pool = list()

    for x in range(nbOrders):
        pool.append("Order #{} - Candy: {}, Amount Ordered: {}, Conditionning: {}".
            format(x + 1, oracle.getRandomCountry(), oracle.getRandomCandy(),
                   oracle.getAmountOrdered(), oracle.getRandomConditionning()))
    
    mongo.saveOrderPool(pool)



