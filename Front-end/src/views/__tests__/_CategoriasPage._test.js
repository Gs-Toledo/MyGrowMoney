import { mount } from '@vue/test-utils'
import { vi } from 'vitest'
import CategoriasView from '@/views/CategoriasPage.vue' // ajuste o caminho conforme necessário
import axiosMyGrowMoney from '@/services/axios-configs'


vi.mock('@/services/axios-configs')

describe('CategoriasView', () => {
  let wrapper

  beforeEach(() => {
   
    wrapper = mount(CategoriasView)
  })

  afterEach(() => {
    vi.clearAllMocks() 
  })

  it('deve exibir o spinner de carregamento enquanto as categorias estão sendo carregadas', async () => {
 
    axiosMyGrowMoney.mockResolvedValue({ data: { categories: [] } })

    await wrapper.vm.getCategorias()

    
    expect(wrapper.find('v-progress-circular').exists()).toBe(true)
  })

  it('deve exibir uma mensagem de erro se a requisição falhar', async () => {
    axiosMyGrowMoney.mockRejectedValue(new Error('Erro ao carregar as categorias'))

    
    await wrapper.vm.getCategorias()

    
    expect(wrapper.text()).toContain('Erro ao carregas os dados, tente novamente mais tarde...')
  })

  it('deve exibir as categorias carregadas', async () => {
    const mockCategorias = [
      { id: 1, name: 'Categoria 1' },
      { id: 2, name: 'Categoria 2' }
    ]
    axiosMyGrowMoney.mockResolvedValue({ data: { categories: mockCategorias } })


    await wrapper.vm.getCategorias()

   
    expect(wrapper.findAll('tr')).toHaveLength(mockCategorias.length)
  })

  it('deve exibir a mensagem "Nenhuma Categoria encontrada." quando não houver categorias', async () => {
    axiosMyGrowMoney.mockResolvedValue({ data: { categories: [] } })

    await wrapper.vm.getCategorias()

    
    expect(wrapper.text()).toContain('Nenhuma Categoria encontrada.')
  })

  it('deve chamar o método de deleteCategoria quando o botão "Deletar" for clicado', async () => {
    const mockCategoria = { id: 1, name: 'Categoria 1' }
    const confirmMock = vi.fn().mockReturnValue(true)
    global.confirm = confirmMock

  
    axiosMyGrowMoney.delete.mockResolvedValue({})

   
    wrapper = mount(CategoriasView, {
      data() {
        return {
          categorias: [mockCategoria],
          isLoading: false,
          hasError: false
        }
      }
    })

    await wrapper.find('button').trigger('click')

   
    expect(axiosMyGrowMoney.delete).toHaveBeenCalledWith('/categories/1')
    expect(confirmMock).toHaveBeenCalled()
  })
})
