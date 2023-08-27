import Lib_Vect_Mat_Complex as lvmc
import unittest

class Test_operations_vector_matriz_complex(unittest.TestCase):

    def test_sum_vector(self):
        sum = lvmc.sum_vector_complex([complex(5, 4), complex(2, 4)],[complex(3, 2), complex(5, 1)])
        self.assertAlmostEqual(sum[0], complex(8,6))
        self.assertAlmostEqual(sum[1], complex(7,5))

    def test_sum_vector2(self):
        sum = lvmc.sum_vector_complex([complex(-5, -5), complex(-4, 4)],[complex(3, 2), complex(5, 1)])
        self.assertAlmostEqual(sum[0], complex(-2,-3))
        self.assertAlmostEqual(sum[1], complex(1,5))

    def test_inv_vector(self):
        inv = lvmc.inv_add_vector_complex([complex(-5, -5), complex(-4, 4)])
        self.assertAlmostEqual(inv[0], complex(5, 5))
        self.assertAlmostEqual(inv[1], complex(4,-4))

    def test_inv_vector2(self):
        inv = lvmc.inv_add_vector_complex([complex(8, -5), complex(-2, 4)])
        self.assertAlmostEqual(inv[0], complex(-8, 5))
        self.assertAlmostEqual(inv[1], complex(2, -4))

    def test_mult_escalar_vector(self):
        mult = lvmc.mult_scalar_vector_complex(5,[complex(5, 4), complex(2, 4)])
        self.assertAlmostEqual(mult[0], complex(25, 20))
        self.assertAlmostEqual(mult[1], complex(10, 20))

    def test_mult_escalar_vector2(self):
        mult = lvmc.mult_scalar_vector_complex(2, [complex(5, 4), complex(2, 4)])
        self.assertAlmostEqual(mult[0], complex(10, 8))
        self.assertAlmostEqual(mult[1], complex(4, 8))

    def test_sum_matrix_complex(self):
        sum = lvmc.sum_matrix_complex([[complex(1, 2), complex(3, -1)],
                                             [complex(0, 4), complex(-2, 5)]],
                                  [[complex(-1, 1), complex(2, 3)],
                                            [complex(0, 6), complex(4, -2)]])
        self.assertAlmostEqual(sum[0][0], complex(0,3))
        self.assertAlmostEqual(sum[0][1], complex(5,2))
        self.assertAlmostEqual(sum[1][0], complex(0,10))
        self.assertAlmostEqual(sum[1][1], complex(2,3))

    def test_sum_matrix_complex2(self):
        sum = lvmc.sum_matrix_complex([[complex(1, 2), complex(3, -1)],
                                       [complex(8, 4), complex(-2, 5)]],
                                      [[complex(-1, 1), complex(2, 3)],
                                       [complex(8, 6), complex(4, -2)]])
        self.assertAlmostEqual(sum[0][0], complex(0, 3))
        self.assertAlmostEqual(sum[0][1], complex(5, 2))
        self.assertAlmostEqual(sum[1][0], complex(16, 10))
        self.assertAlmostEqual(sum[1][1], complex(2, 3))

    def test_inv_matrix_complex(self):
        inv = lvmc.inv_add_matrix_complex([[complex(1, 2), complex(3, -1)],
                                            [complex(8, 4), complex(-2, 5)]])
        self.assertAlmostEqual(inv[0][0], complex(-1, -2))
        self.assertAlmostEqual(inv[0][1], complex(-3, 1))
        self.assertAlmostEqual(inv[1][0], complex(-8, -4))
        self.assertAlmostEqual(inv[1][1], complex(2, -5))

    def test_inv_matrix_complex2(self):
        inv = lvmc.inv_add_matrix_complex([[complex(-5, 2), complex(3, -1)],
                                           [complex(-2, -9), complex(-2, 5)]])
        self.assertAlmostEqual(inv[0][0], complex(5, -2))
        self.assertAlmostEqual(inv[0][1], complex(-3, 1))
        self.assertAlmostEqual(inv[1][0], complex(2, 9))
        self.assertAlmostEqual(inv[1][1], complex(2, -5))

    def test_mult_escalar_matrix_complex(self):
        inv = lvmc.mult_scalar_matrix_complex(5, [[complex(1, 2), complex(3, -1)],
                                                                [complex(0, 4), complex(-2, 5)]])
        self.assertAlmostEqual(inv[0][0], complex(5, 10))
        self.assertAlmostEqual(inv[0][1], complex(15, -5))
        self.assertAlmostEqual(inv[1][0], complex(0, 20))
        self.assertAlmostEqual(inv[1][1], complex(-10, 25))

    def test_mult_escalar_matrix_complex2(self):
        inv = lvmc.mult_scalar_matrix_complex(4, [[complex(1, 2), complex(3, -1)],
                                                                [complex(0, 4), complex(-2, 5)]])
        self.assertAlmostEqual(inv[0][0], complex(4, 8))
        self.assertAlmostEqual(inv[0][1], complex(12, -4))
        self.assertAlmostEqual(inv[1][0], complex(0, 16))
        self.assertAlmostEqual(inv[1][1], complex(-8, 20))

    def test_trasp_matrix_complex(self):
        trasp = lvmc.transpose_matrix_complex([complex(1, 2), complex(3, -5)])
        self.assertAlmostEqual(trasp[0][0], complex(1, 2))
        self.assertAlmostEqual(trasp[1][0], complex(3, -5))

    def test_trasp_matrix_complex2(self):
        trasp = lvmc.transpose_matrix_complex([[complex(1, 2), complex(3, -1)],
                                                [complex(0, 4), complex(-2, 5)]])
        self.assertAlmostEqual(trasp[0][0], complex(1, 2))
        self.assertAlmostEqual(trasp[0][1], complex(0, 4))
        self.assertAlmostEqual(trasp[1][0], complex(3, -1))
        self.assertAlmostEqual(trasp[1][1], complex(-2, 5))

    def test_conj_matrix_complex(self):
        conj = lvmc.conjugate_matrix([complex(1, 2), complex(3, -5)])
        self.assertAlmostEqual(conj[0], complex(1, -2))
        self.assertAlmostEqual(conj[1], complex(3, 5))

    def test_conj_matrix_complex2(self):
        conj = lvmc.conjugate_matrix([[complex(1, 2), complex(3, -1)],
                                        [complex(0, 4), complex(-2, 5)]])
        self.assertAlmostEqual(conj[0][0], complex(1, -2))
        self.assertAlmostEqual(conj[0][1], complex(3, 1))
        self.assertAlmostEqual(conj[1][0], complex(0, -4))
        self.assertAlmostEqual(conj[1][1], complex(-2, -5))

    def test_adj_matrix_complex(self):
        adj = lvmc.adjoint_matrix([complex(1, 2), complex(3, -5)])
        self.assertAlmostEqual(adj[0][0], complex(1, -2))
        self.assertAlmostEqual(adj[1][0], complex(3,+5))

    def test_adj_matrix_complex2(self):
        adj = lvmc.adjoint_matrix([[complex(1, 2), complex(3, -1)],
                                    [complex(0, 4), complex(-2, 5)]])
        self.assertAlmostEqual(adj[0][0], complex(1, -2))
        self.assertAlmostEqual(adj[0][1], complex(0, -4))
        self.assertAlmostEqual(adj[1][0], complex(3, 1))
        self.assertAlmostEqual(adj[1][1], complex(-2, -5))

    def test_mult_matrix(self):
        mult = lvmc.mult_matrix([[complex(1, 2), complex(3, -1)],
                                   [complex(0, 4), complex(-2, 5)]],
                            [[complex(-1, 1), complex(2, 3)],
                                   [complex(0, 6), complex(4, -2)]])
        self.assertAlmostEqual(mult[0][0], complex(3, 17))
        self.assertAlmostEqual(mult[0][1], complex(6, -3))
        self.assertAlmostEqual(mult[1][0], complex(-34, -16))
        self.assertAlmostEqual(mult[1][1], complex(-10, 32))

    def test_mult_matrix2(self):
        mult = lvmc.mult_matrix([[complex(1, 2), complex(3, -1)],
                                 [complex(8, 4), complex(-2, 5)]],
                                [[complex(-1, 1), complex(2, 3)],
                                 [complex(8, 6), complex(4, -2)]])
        self.assertAlmostEqual(mult[0][0], complex(27, 9))
        self.assertAlmostEqual(mult[0][1], complex(6, -3))
        self.assertAlmostEqual(mult[1][0], complex(-58, 32))
        self.assertAlmostEqual(mult[1][1], complex(6, 56))

    def test_matriz_action_vector(self):
        action = lvmc.matrix_action_vector([[complex(1, 2), complex(3, -1)],
                                                [complex(0, 4), complex(-2, 5)]],
                                        [complex(-1, 1), complex(2, 3)])
        self.assertAlmostEqual(action[0], complex(6, 6))
        self.assertAlmostEqual(action[1], complex(-23, 0))

    def test_matriz_action_vector2(self):
        action = lvmc.matrix_action_vector([[complex(1, 2), complex(3, 4)],
                                            [complex(8, 4), complex(-2, 5)]],
                                           [complex(-1, 1), complex(2, 3)])
        self.assertAlmostEqual(action[0], complex(-9, 16))
        self.assertAlmostEqual(action[1], complex(-31, 8))

if __name__ == '__main__':
    unittest.main()
